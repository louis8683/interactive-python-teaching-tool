import inspect
from types import FrameType, MethodType, ModuleType
from copy import Error, deepcopy
import pickle
import types
import builtins
from typing import Any

# insert "[command]" into every line
# search the output for our tag
first_line = "import inspect; from find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe());\n"
command_start = "fvc.update(inspect.currentframe(), 'start'); "
command_end = "; fvc.update(inspect.currentframe(), 'end')"
command_return = "fvc.update(inspect.currentframe(), 'return'); "
command_empty = "fvc.update(inspect.currentframe(), 'empty')"
last_line = "fvc.save_to_file('_temp.pickle')\n"

# all built in types, used to distinguish custom class from builtin types
builtin_types = set()
for builtin_type in builtins.__dict__.values():
    try:
        builtin_types.add(builtin_type)
    except TypeError: # unhashable types
        continue

class ModuleTypeCopy:
    def __init__(self, module: types.ModuleType):
        self._str = module.__str__()
        self._repr = module.__repr__()
    
    def __eq__(self, o: object) -> bool:
        return self._str == str(o) and self._repr == repr(o)

    def __str__(self) -> str:
        return self._str
    
    def __repr__(self) -> str:
        return self._repr

class CustomClassCopy:
    '''A replacement for custom classes to remove __main__ from the class definition/instances.
    Otherwise, we need to import the file we just executed when we load our pickle to analyze.'''
    def __init__(self, obj):
        self.class_name = repr(obj.__class__).split(".")[-1][:-2]
        try:
            self.hash = obj.__hash__()
            self.vars = obj.__dict__.copy()
        except TypeError: # descriptor '__hash__' of 'object' object needs an argument
            # This is the class definition, not an instance (<class 'type'>)
            self.hash = None
            self.vars = {}
        
    def __eq__(self, o) -> bool:
        try:
            return self.hash == o.hash
        except TypeError or AttributeError: # NoneType not hashable
            return False
    
    def __repr__(self):
        return f"<class '{self.class_name}'(dummy)> with hash {self.hash}"

def replace_main_recursively(obj):
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
                    cpy.vars[varname] = replace_main_recursively(cpy.vars[varname])
            except AttributeError:
                pass
    return cpy

class FindVariableChanges:
    def __init__(self, frame: FrameType):
        self.frame = frame
        self.last_frame = frame
        self.record: dict = []
        self.update(frame, "init")

    def update(self, frame: FrameType, cmd_position: str):
        print(frame.f_lineno)
        # store parameter into this class object
        self.frame = self._FrameTypeCopy(frame, should_convert_module=True)

        # swap custom types into CustomClassCopy
        for var_name in self.frame.f_globals:
            self.frame.f_globals[var_name] = replace_main_recursively(self.frame.f_globals[var_name])
        for var_name in self.frame.f_locals:
            self.frame.f_locals[var_name] = replace_main_recursively(self.frame.f_locals[var_name])
        
        if self.frame.f_lineno == 38:
            print(self.frame.f_globals)

        # calculate difference
        diff = self._diff_of_vars()

        # update record and last_frame
        self.record.append({"diff": diff, "line_no": int(frame.f_lineno) - 1, "frame": self.frame, "position": cmd_position})
        self.last_frame = self.frame
    
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

    class _FrameTypeCopy:
        '''FrameType cannot be copied, and is mutable. Thus we created a custom 
        type to store the last frame.
        Convert modules to strings so this class can be pickled/deepcopied.'''
        def __init__(self, frame: FrameType, should_convert_module=True):
            # deepcopy cannot pickle modules, so we use custom copy
            self.f_globals = self._copy_dict(frame.f_globals, convert=should_convert_module)
            self.f_locals = self._copy_dict(frame.f_locals, convert=should_convert_module)
            self.f_lineno = deepcopy(frame.f_lineno)
        
        def module_as_str(self):
            '''All the module value converted to dummy module type _ModuleTypeCopy'''
            def convert(target: dict):
                for key in target:
                    # Find all the modules
                    if type(target[key]) == types.ModuleType:
                        # Turn them into strings
                        target[key] = ModuleTypeCopy(target[key])
            convert(self.f_globals)
            convert(self.f_locals)
        
        def _copy_dict(self, source: dict, convert=False):
            # when we meet a module, we don't deepcopy
            new_copy = {}
            for key in source:
                # NOTE: (important) don't copy class FindVariableChanges, record will be recursively put into memory
                if key in ('fvc', 'FVC', 'FindVariableChanges'):
                    continue
                # Module type
                elif type(source[key]) == types.ModuleType:
                    # TODO: nested module is not checked.
                    if convert:
                        new_copy[key] = ModuleTypeCopy(source[key])
                    else:
                        new_copy[key] = source[key]
                # Class type
                elif type(source[key]) not in builtin_types:
                    new_copy[key] = source[key]
                else:
                    new_copy[key] = deepcopy(source[key])
            return new_copy
    
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
