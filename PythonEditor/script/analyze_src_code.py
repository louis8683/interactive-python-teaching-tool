# Usage: python analyze_src_code.py [src_filename] [target_json]

from typing import Any
import pickle
import os
import sys
import re
from copy import deepcopy

from script.find_variable_changes import FindVariableChanges
import script.source_code_parser as scp
import script.script_rewriter as sr

input_list_pickle_filename = "input.pickle"
pickle_filename = "_temp.pickle"

class SourceCodeAnalyzer:
    def __init__(self, filename, line_no_start=1, input_list:list=[]):
        self.offset = line_no_start
        self.src_filename = filename
    
        # Load parser
        self.parser = scp.SourceCodeParser(self.src_filename)
        
        self.rerun(input_list)
    
    def rerun(self, input_list:list[str]=[]):
        '''This function is isolated to provide interactivity when input() is used.
        This function '''
        # Pickle the input_list
        with open(input_list_pickle_filename, "+wb") as file:
            pickle.dump(input_list, file)

        # Mine data
        self.fvc = self.extract_data_from_source_file()

        # Analyze
        self.actions = self.analyze(self.fvc)

    def extract_data_from_source_file(self, delete_intermediate_files=True) -> FindVariableChanges:
        # Rewrite file
        rewriter = sr.ScriptRewriter(self.src_filename)
        rewriter.run()

        # Execute rewritten file 
        # NOTE: better way to properly execute the rewritten file?
        generated_file_name = rewriter.generated_filename
        os.system(f"python {generated_file_name}")

        # Load the fvc from the generated pickle
        with open(pickle_filename, "rb") as file:
            fvc = pickle.load(file)
        
        # Delete rewritten file and pickle
        if delete_intermediate_files:
            os.remove(generated_file_name)
            os.remove(pickle_filename)
            os.remove(input_list_pickle_filename)
        
        return fvc
    
    def analyze(self, fvc: FindVariableChanges) -> list:
        # Parse records into action of each line
        actions: list[int,dict,int] = [] # (line_no, events, record_no)
        
        # Lambdas for quick access
        g_deleted = lambda i: fvc.record[i]['diff']['global']['deleted']
        g_added = lambda i: fvc.record[i]['diff']['global']['added']
        g_changed = lambda i: fvc.record[i]['diff']['global']['changed']
        l_deleted = lambda i: fvc.record[i]['diff']['local']['deleted']
        l_added = lambda i: fvc.record[i]['diff']['local']['added']
        l_changed = lambda i: fvc.record[i]['diff']['local']['changed']
        
        i = 1 # Ignore 0th line (command from fvc)
        line_max_seen = 0
        while i < len(fvc.record):

            # Special Case: input()
            if "status" in fvc.record[i] and fvc.record[i]["status"] == "need input":
                actions.append(("need input", fvc.record[i]["input"]))
                return actions
            
            # Case 1: function or class definition.
            # Pattern: line_no jumped forward to unseen line
            if fvc.record[i]['line_no'] > fvc.record[i-1]['line_no'] and fvc.record[i]['line_no'] > line_max_seen:
                # Check next lines of last executed line for [def] or [class]
                for target_line in range(fvc.record[i-1]['line_no'] + 1, fvc.record[i]['line_no']):    
                    for start, end, indentation, keyword in self.parser.code_blocks:
                        keyword_line = start - 1
                        if keyword_line == target_line and keyword in ("def", "class") and self.parser.indentations[keyword_line] == self.parser.indentations[fvc.record[i-1]['line_no']]:
                            actions.append((target_line, {keyword: self.parser.lines[start - 1]}, i-1))
            line_max_seen = max(line_max_seen, fvc.record[i]['line_no'])

            # Case 2: variable added/deleted/changed in this line
            # Not including jumping commands, such as function calls (including class instantiation calling __init__())
            
            # Create a dict for the events of this line
            events = {}
            # only locate rear commands
            if fvc.record[i]['position'] == "end": # rear command
                # identify variable modification
                if g_deleted(i):
                    events["g_deleted"] = g_deleted(i)
                if g_added(i):
                    events["g_added"] = g_added(i)
                if g_changed(i):
                    changed: dict[str, tuple[Any, Any]] = {} # (old, new)
                    for var_name in g_changed(i):
                        changed[var_name] = (fvc.record[i-1]['frame'].f_globals[var_name], fvc.record[i]['frame'].f_globals[var_name])
                    events["g_changed"] = changed
                if l_deleted(i):
                    events["l_deleted"] = l_deleted(i)
                if l_added(i):
                    events["l_added"] = l_added(i)
                if l_changed(i):
                    changed: dict[str, tuple[Any, Any]] = {} # (old, new)
                    for var_name in l_changed(i):
                        changed[var_name] = (fvc.record[i-1]['frame'].f_locals[var_name], fvc.record[i]['frame'].f_locals[var_name])
                    events["l_changed"] = changed
            
            # TODO: Case 3: return

            # TODO: Case 4: for loop (ex: for i in range(10), the i is a variable)

            # Case 5: print/input
            # only locate rear commands
            if fvc.record[i]['position'] == "end": # rear command
                # Find print tag
                if "print" in fvc.record[i]:
                    events["print"] = fvc.record[i]["print"]
                if "input" in fvc.record[i]:
                    events["input"] = fvc.record[i]["input"]

            # TODO: Case 6: input
                
            # Append actions
            if i == len(fvc.record) - 1 or fvc.record[i]['position'] in ("empty", "end"):
                actions.append((fvc.record[i]['line_no'], events, i))
            
            # Increment i
            i += 1
        return actions
    
    def get_variables(self, record_no: int, remove_dunder=True, remove_names=["inspect", "print", "input"]):
        g_vars = self.fvc.record[record_no]['frame'].f_globals
        l_vars = self.fvc.record[record_no]['frame'].f_locals
        if remove_dunder:
            for var_name in deepcopy(g_vars):
                if re.match("__.*__", var_name) or var_name in remove_names:
                    del g_vars[var_name]
            for var_name in deepcopy(l_vars):
                if re.match("__.*__", var_name) or var_name in remove_names:
                    del l_vars[var_name]
        return {"global": g_vars, "local": l_vars}



if __name__ == "__main__":
    # Read filename from command line
    src_file = sys.argv[1]
    analyzer = SourceCodeAnalyzer(src_file)
    for action in analyzer.actions:
        input()
        print(action)
