import inspect; from script.find_variable_changes import FindVariableChanges as FVC; fvc = FVC(inspect.currentframe()); print = fvc.print; input = fvc.input;
# Let's write a simple recursion
def deep_add(obj:list):
    # End condition, return 0 if empty
    if len(obj) == 0:
        fvc.update(inspect.currentframe(), 'return'); return 0
    
    # This is a recursive deep add function
    fvc.update(inspect.currentframe(), 'start'); sum = 0; fvc.update(inspect.currentframe(), 'end')
    for element in obj:
        if type(element) in (tuple, list):
            fvc.update(inspect.currentframe(), 'start'); sum += deep_add(element); fvc.update(inspect.currentframe(), 'end')
        elif type(element) in (int, float):
            fvc.update(inspect.currentframe(), 'start'); sum += element; fvc.update(inspect.currentframe(), 'end')
    
    # Return sum
    fvc.update(inspect.currentframe(), 'return'); return sum

fvc.update(inspect.currentframe(), 'start'); deep_list = [[1,1],1,1]; fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); answer = deep_add(deep_list); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print(answer); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print("Hello"); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print("World"); fvc.update(inspect.currentframe(), 'end')
fvc.update(inspect.currentframe(), 'start'); print("!!"); fvc.update(inspect.currentframe(), 'end')
fvc.save_to_file('_temp.pickle')
