import inspect; from find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe());
from pprint import pprint; fvc.update(inspect.currentframe())
from time import sleep; fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
var_names = [i for i in locals().keys() if i[:2] != "__"]; fvc.update(inspect.currentframe())
for var_name in var_names:
    print(var_name, type(locals()[var_name])); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
pprint(f"Hello world! Yo Yo Yo"); fvc.update(inspect.currentframe())
print("你好，世界😀"); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
def add(i, j):
    fvc.update(inspect.currentframe())
    sum = i + j; fvc.update(inspect.currentframe())
    return sum; fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
class CC:
    fvc.update(inspect.currentframe())
    def __init__(self):
        self.name = "Cool!"; fvc.update(inspect.currentframe())
        self.age = "1000"; fvc.update(inspect.currentframe())
        self.description = "ooold"; fvc.update(inspect.currentframe())
        print(f"G:{globals().keys()}"); fvc.update(inspect.currentframe())
        print(f"L:{locals().keys()}"); fvc.update(inspect.currentframe())
        print(f"D:{dir(self)}"); fvc.update(inspect.currentframe())
    fvc.update(inspect.currentframe())
    def scream(self):
        print(self.name); fvc.update(inspect.currentframe())
        fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
li = []; fvc.update(inspect.currentframe())
for i in range(10):
    li.append(i); fvc.update(inspect.currentframe())
    li.append(0); fvc.update(inspect.currentframe())
print(li); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
print(add(1,2)); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
if 10 == 10:
    print("Correct"); fvc.update(inspect.currentframe())
else:
    print("Incorrect"); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
cc = CC(); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
var_names = [i for i in locals().keys() if i[:2] != "__"]; fvc.update(inspect.currentframe())
for var_name in var_names:
    print(var_name, type(locals()[var_name])); fvc.update(inspect.currentframe())
fvc.update(inspect.currentframe())
print(globals()); fvc.update(inspect.currentframe())
fvc.save_to_file('_temp.pickle')
