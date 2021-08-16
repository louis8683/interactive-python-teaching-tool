from find_code_blocks import find_code_blocks_with_file
import pickle
import os
from find_variable_changes import FindVariableChanges as FVC

# Q: how to properly load the classes of the file?
src_file = "test2.py"
exec(f"from {src_file[:src_file.rfind('.py')]} import *")

# Q: how to properly execute the rewritten file
import os
os.system(f"python _{src_file}_temp.py")

fvc: FVC = None

# Load the fvc
pickle_filename = "_temp.pickle"
with open(pickle_filename, "rb") as file:
    fvc = pickle.load(file)

# Check records
for i, record in enumerate(fvc.record): 
    # Ignore first line (command from fvc)
    if i == 0: 
        continue
    
    # input() # wait for key to continue
    
    # Line no, minus 1 to remove add line of command in the _temp python script.
    print(f"line {record['line_no'] - 1}", end=" ")

    # Globals
    print("G_vars", end=" ")
    # Deleted vars
    g_deleted = record['diff']['global']['deleted']
    if g_deleted:
        print(f"D: {list(g_deleted)}", end=" ")
    g_added = record['diff']['global']['added']
    if g_added:
        print(f"A: {list(g_added)}", end=" ")
    g_changed = record['diff']['global']['changed']
    if g_changed:
        print(f"C:", end=" ")
        for var_name in g_changed:
            print(f"{var_name}({fvc.record[i-1]['frame'].f_globals[var_name]}->{record['frame'].f_globals[var_name]})", end=" ")
    
    print(" ")

# Parse records into action of each line
actions = []
# Lambdas for quick access
g_deleted = lambda rec: rec['diff']['global']['deleted']
g_added = lambda rec: rec['diff']['global']['added']
g_changed = lambda rec: rec['diff']['global']['changed']
# Acquire the code block info
codeblocks = find_code_blocks_with_file(src_file)

i = 1 # Ignore 0th line (command from fvc)
while i < len(fvc.record):
    # Create a dict for the events of this line
    events = {}

    line_no = fvc.record[i]['line_no']

    # Case 1: variable added/deleted/changed in this line
    # Not including jumping commands, such as function calls (including class instantiation calling __init__())

    # locate rear commands
    if fvc.record[i]['position'] == "end": # rear command
        g_deleted = fvc.record[i]['diff']['global']['deleted']
        g_added = fvc.record[i]['diff']['global']['added']
        g_changed = fvc.record[i]['diff']['global']['changed']
        # identify variable modification
        if g_deleted:
            events["g_deleted"] = g_deleted
        if g_added:
            events["g_added"] = g_added
        if g_changed:
            events["g_changed"] = g_changed
    
    # Case 2: function or class definition.
    # Pattern: jumps forward, from rear cmd to start cmd.
    # Jumps forward and next record jumps from a rear cmd to a start cmd?
    if line_no - fvc.record[i-1]['line_no'] > 1 and fvc.record[i]['position'] == "start" and fvc.record[i-1]['position'] == "end":
        # TODO: Ignore if/while/for code blocks
        # find missing code block with definition
        candid, selected = [], []
        for codeblock in codeblocks:
            # only select outer most definitions
            if fvc.record[i-1]['line_no'] - 1 < codeblock[0] < line_no - 1:
                candid.append(codeblock)
        # if such code block exist
        if len(candid):    
            # sort candid
            candid.sort()
            print(candid)
            # remove nested ones
            current_end = candid[0][1]
            selected.append(candid[0])
            for codeblock in candid:
                if current_end < codeblock[0]:
                    selected.append(codeblock)
                    current_end = codeblock[1]
            # Append actions
            for codeblock in selected:
                actions.append((codeblock[0], "Case 2"))
        
    # Append actions
    if i == len(fvc.record) - 1 or fvc.record[i]['position'] in ("empty", "end"):
        actions.append((line_no - 1, events))
    
    # Increment i
    i += 1

for action in actions:
    input()
    print(action)