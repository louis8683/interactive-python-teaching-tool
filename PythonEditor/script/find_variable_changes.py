import inspect
from types import FrameType, ModuleType
import pickle
import builtins
from typing import Any
import sys

from script.custom_types import ModuleTypeCopy, CustomClassCopy, FrameTypeCopy, CustomStdout

pickle_name = "_temp.pickle"
# insert "[command]" into every line
# search the output for our tag
first_lines = [
    "import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); import sys; sys.stdout = fvc.stdout; input = fvc.input;\n",
    "try:\n"]
leading_spaces = "    "
command_start = "fvc.update(inspect.currentframe(), 'start'); "
command_end = "; fvc.update(inspect.currentframe(), 'end')"
command_return = "fvc.update(inspect.currentframe(), 'return'); "
command_empty = "fvc.update(inspect.currentframe(), 'empty')"
last_lines = [
    f"    fvc.save_to_file('{pickle_name}')\n",
    f"except Exception as e:\n",
    f"    fvc.on_error(e)\n"]

# all built in types, used to distinguish custom class from builtin types
builtin_types = set()
for builtin_type in builtins.__dict__.values():
    try:
        builtin_types.add(builtin_type)
    except TypeError: # unhashable types
        continue

# TODO: file I/O (cannot use relative path)

class FindVariableChanges:
    def __init__(self, frame: FrameType):
        self.frame = frame
        self.last_frame = frame
        self.record: dict = []
        self.stdout = CustomStdout()
        self.pending_input = None
        self.inserted_lines: int = 1

        # Load the input list
        with open("input.pickle", "rb") as file:
            self.input_list = pickle.load(file)

        self.update(frame, "init")

    def update(self, frame: FrameType, cmd_position: str):
        # store parameter into this class object
        self.last_frame = self.frame
        self.frame = FrameTypeCopy(frame, should_convert_module=True)

        # swap custom types into CustomClassCopy
        for var_name in self.frame.f_globals:
            self.frame.f_globals[var_name] = self._replace_main_recursively(self.frame.f_globals[var_name])
        for var_name in self.frame.f_locals:
            self.frame.f_locals[var_name] = self._replace_main_recursively(self.frame.f_locals[var_name])

        # calculate difference
        diff = self._diff_of_vars()

        # update record
        record = {"diff": diff, "line_no": int(frame.f_lineno) - len(first_lines), "frame": self.frame, "position": cmd_position}
        if self.stdout.pending: # add print tag if pending
            record["print"] = self.stdout.read_all(clear=True)
        if self.pending_input is not None: # add input tag if pending
            record["input"] = self.pending_input
            self.pending_input = None
        self.record.append(record)
    
    def save_to_file(self, filename: str):
        '''Pickle this class into a file with [filename].
        Note that self.frame self.last_frame are not pickled, since a module cannot be pickled.'''
        frame = self.frame
        last_frame = self.last_frame
        with open(filename, "wb+") as file:
            del self.frame
            del self.last_frame
            pickle.dump(self, file)
        self.frame = frame
        self.last_frame = last_frame
    
    def input(self, prompt=""):
        '''Override input(). Use this method (instead of redirecting [sys.stdin]) to display the prompt in the UI.'''
        self.pending_input = str(prompt)
        # Input list contains user input
        if len(self.input_list) > 0:
            return self.input_list.pop(0)
        # Input list is empty (exit execution to prompt more inputs)
        else:
            # Add a tag to the record
            self.record.append({"status": "need input", "input": str(prompt), "line_no": int(self.frame.f_lineno) - len(first_lines)})
            # Pickle the current progress
            self.save_to_file(pickle_name)
            # Exit
            sys.exit(1)

    def on_error(self, error: Exception):
        '''Called when unhandled error occured (handled by last except block of rewritten code).'''
        # Add a tag to the record
        self.record.append({"status": "error", "error": error, "line_no": int(self.frame.f_lineno) - len(first_lines)})
        # Pickle the current progress
        self.save_to_file(pickle_name)
        # Exit
        sys.exit(1)
    
    def _replace_main_recursively(self, obj):
        ''' __main__.[Custom Class Name] type require executing in __main__. Replace this 
        with a custom class copy dummy type to not have to import the file when we are
        analyzing the frames.
        '''
        try:
            if obj.__module__ != "__main__":
                return obj
        except AttributeError:
            return obj
        
        cpy = CustomClassCopy(obj)
        for varname in cpy.vars:
            if type(cpy.vars[varname]) == ModuleType:
                cpy.vars[varname] = ModuleTypeCopy(cpy.vars[varname])
            else:
                try:
                    if cpy.vars[varname].__module__ == "__main__":
                        cpy.vars[varname] = self._replace_main_recursively(cpy.vars[varname])
                except AttributeError:
                    pass
        return cpy

    
    def _user_defined_vars(self, frame: FrameType):
        global_vars = [key for key in frame.f_globals.keys() if key[:2] != "__"]
        local_vars = [key for key in frame.f_locals.keys() if key[:2] != "__" and key not in global_vars]
        return (global_vars, local_vars)
    
    def _diff_of_vars(self) -> dict[str,dict[str,set[str]]]:
        '''This function checks for variable changes by comparing last_frame and frame.
        Return value is a dictionary of dictionary str->str->set[str].

        Starting from outside in "val = dict[1st][2nd]"
        1st layer: two keys, "global" and "local"
        2nd layer: three keys, "deleted", "added", and "changed"
        value: a [set] of variable names (str) in the category described by the above two keys.
        
        example usage:
        diff = self._diff_of_vars()
        new_local_vars_set = diff["local"]["added]
        for local_var in new_local_vars_set:
            print(f"new var {local_var} with value {self.frame.f_locals[local_var]}")
        '''
        g_old, l_old = self._user_defined_vars(self.last_frame)
        g_old, l_old = set(g_old), set(l_old)
        g_new, l_new = self._user_defined_vars(self.frame)
        g_new, l_new = set(g_new), set(l_new)

        def diff(old: set, new: set, old_dict: dict, new_dict: dict):
            deleted = old - new
            added = new - old
            changed = new.intersection(old)
            for key in changed.copy():
                if old_dict[key] == new_dict[key]:
                    changed.remove(key)
            return {"deleted": deleted, "added": added, "changed": changed}
        
        g_sets = diff(g_old, g_new, self.last_frame.f_globals, self.frame.f_globals)
        l_sets = diff(l_old, l_new, self.last_frame.f_locals, self.frame.f_locals)
        return {"global": g_sets, "local": l_sets}

if __name__ == "__main__":
    fvc = FindVariableChanges(inspect.currentframe())
    a = 1 + 1; fvc.update(inspect.currentframe())
    b = 2 + 2; fvc.update(inspect.currentframe())
    fvc.update(inspect.currentframe())
    def add(i, j):
        sum = i + j; fvc.update(inspect.currentframe())
        return sum
    fvc.update(inspect.currentframe())
    b = 3 + 3; fvc.update(inspect.currentframe())
    added = add(a, b); fvc.update(inspect.currentframe())
    print(added); fvc.update(inspect.currentframe())
