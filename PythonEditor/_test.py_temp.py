import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); print = fvc.print; input = fvc.input;
fvc.update(inspect.currentframe(), 'start'); i = input("A number please!"); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print(i); fvc.update(inspect.currentframe(), 'end')
fvc.save_to_file('_temp.pickle')
