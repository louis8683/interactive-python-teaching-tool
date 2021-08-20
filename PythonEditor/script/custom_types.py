from sys import stdout
import types
import builtins
from io import TextIOBase
from copy import deepcopy
from typing import Iterable

# all built in types, used to distinguish custom class from builtin types
builtin_types = set()
for builtin_type in builtins.__dict__.values():
    try:
        builtin_types.add(builtin_type)
    except TypeError:
        continue


class ModuleTypeCopy:
    '''Module type cannot be pickled, thus we create a picklable dummy version.'''
    def __init__(self, module: types.ModuleType):
        self._str = module.__str__()
        self._repr = module.__repr__()
    
    def __eq__(self, o: object) -> bool:
        return self._str == str(o) and self._repr == repr(o)

    def __str__(self) -> str:
        return self._str
    
    def __repr__(self) -> str:
        return self._repr


# __main__.[Custom Class Name] type require executing in __main__. Replace this 
# with a custom class copy dummy type to not have to import the file when we are
# analyzing the frames.
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


class FrameTypeCopy:
    '''FrameType cannot be copied, and is mutable. Thus we created a custom 
    type to store the last frame.
    Convert modules to strings so this class can be pickled/deepcopied.'''
    def __init__(self, frame: types.FrameType, should_convert_module=True):
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

class CustomStdout(TextIOBase):
    '''This class provides a container for redirecting sys.stdout.
    
    usage: 
    > import sys
    > orig_stdout = sys.stdout # Keep a referece of the original.
    > sys.stdout = custom_stdout = CustomStdout() # Redirect stdout
    '''
    def __init__(self):
        super().__init__()
        self.history: list[str] = []
        self.log = []
        self.pending = False
    
    # Override TextIOBase functions.

    def write(self, __s: str) -> int:
        self.pending = True
        self.history.append(__s)
        self.log.append({"write": __s})
        return len(__s)
    
    def writelines(self, __lines: Iterable[str]) -> None:
        self.log.append({"writelines": __lines})
        for line in __lines:
            self.write(line)

    # Custom functions.

    def clear(self) -> None:
        '''Clears history and log.'''
        self.history, self.log = [], []
        self.pending = False

    def read_all(self, clear: bool=True) -> str:
        s = "".join(self.history)
        if clear:
            self.clear()
        return s

if __name__ == "__main__":
    import sys
    stdout = sys.stdout
    sys.stdout = custom_stdout = CustomStdout()
    print("Hi")
    print("Hello")
    sys.stdout = stdout
    print("Everything:")
    print(custom_stdout.read_all())
