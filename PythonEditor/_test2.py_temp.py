import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); print = fvc.print; input = fvc.input;
fvc.update(inspect.currentframe(), 'start'); from pprint import pprint; fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); from time import sleep; fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); pprint(f"Hello world! Yo Yo Yo"); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print("你好，世界😀"); fvc.update(inspect.currentframe(), 'end')
def add(i, j):
    fvc.update(inspect.currentframe(), 'start'); sum = i + j; fvc.update(inspect.currentframe(), 'end')
    fvc.update(inspect.currentframe(), 'return'); return sum

class CC:
    def __init__(self):
        fvc.update(inspect.currentframe(), 'start'); self.name = "Cool!"; fvc.update(inspect.currentframe(), 'end')
        fvc.update(inspect.currentframe(), 'start'); self.age = "1000"; fvc.update(inspect.currentframe(), 'end')
        fvc.update(inspect.currentframe(), 'start'); self.description = "ooold"; fvc.update(inspect.currentframe(), 'end')
    
    def scream(self):
        fvc.update(inspect.currentframe(), 'start'); print(self.name); fvc.update(inspect.currentframe(), 'end')
    
    class InnerCC:
        def __init__(self):
            fvc.update(inspect.currentframe(), 'start'); print("shy..."); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); li = []; fvc.update(inspect.currentframe(), 'end')
for i in range(10):
    fvc.update(inspect.currentframe(), 'start'); li.append(i); fvc.update(inspect.currentframe(), 'end')
    fvc.update(inspect.currentframe(), 'start'); li.append(0); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print(li); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); print(add(1,2)); fvc.update(inspect.currentframe(), 'end')

if 10 == 10:
    fvc.update(inspect.currentframe(), 'start'); print("Correct"); fvc.update(inspect.currentframe(), 'end')
else:
    fvc.update(inspect.currentframe(), 'start'); print("Incorrect"); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); cc = CC(); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); cc.scream(); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); cc = CC(); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); innerCC = cc.InnerCC(); fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); cc.scream(); fvc.update(inspect.currentframe(), 'end')

if 10 == 10:
    fvc.update(inspect.currentframe(), 'start'); print("Correct"); fvc.update(inspect.currentframe(), 'end')
else:
    fvc.update(inspect.currentframe(), 'start'); print("Incorrect"); fvc.update(inspect.currentframe(), 'end')
fvc.save_to_file('_temp.pickle')
