import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); import sys; sys.stdout = fvc.stdout; input = fvc.input;
try:
    fvc.update(inspect.currentframe(), 'start'); from pprint import pprint; fvc.update(inspect.currentframe(), 'end')
    
    fvc.update(inspect.currentframe(), 'start'); a = int(input("Please input a number: ")); fvc.update(inspect.currentframe(), 'end')
    
    fvc.update(inspect.currentframe(), 'start'); a = [a] * 10; fvc.update(inspect.currentframe(), 'end')
    
    fvc.update(inspect.currentframe(), 'start'); pprint(a); fvc.update(inspect.currentframe(), 'end')
    fvc.save_to_file('_temp.pickle')
except Exception as e:
    fvc.on_error(e)
