import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); print = fvc.print; input = fvc.input;
fvc.update(inspect.currentframe(), 'start'); import numpy as np; fvc.update(inspect.currentframe(), 'end')

fvc.update(inspect.currentframe(), 'start'); a = np.array([1,2,3,4,5]); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print(a); fvc.update(inspect.currentframe(), 'end')
fvc.save_to_file('_temp.pickle')
