# Usage: python analyze_src_code.py [src_filename] [target_json]

from typing import Any
import pickle
import os
import sys
import json

from find_variable_changes import FindVariableChanges
import source_code_parser as scp
import script_rewriter as sr

class SourceCodeAnalyzer:
    def __init__(self, filename="", line_no_start=1):
        self.offset = line_no_start
        if filename:
            # Mine data
            self.extract_data_from_source_file(filename)
                        
            # Load parser
            self.parser = scp.SourceCodeParser(self.src_filename)

            # Analyze
            self.actions = self.analyze(self.fvc)

    def extract_data_from_source_file(self, filename, delete_intermediate_files=False):
        self.src_filename = filename
        
        # Rewrite file
        rewriter = sr.ScriptRewriter(self.src_filename)
        rewriter.run()

        # Execute rewritten file 
        # NOTE: better way to properly execute the rewritten file?
        generated_file_name = rewriter.generated_filename
        os.system(f"python {generated_file_name}")

        # Load the fvc from the generated pickle
        self.fvc: FindVariableChanges = None
        pickle_filename = "_temp.pickle"
        with open(pickle_filename, "rb") as file:
            self.fvc = pickle.load(file)
        
        # Delete rewritten file and pickle
        if delete_intermediate_files:
            os.remove(generated_file_name)
            os.remove(pickle_filename)
    
    def analyze(self, fvc: FindVariableChanges) -> list:
        # Parse records into action of each line
        actions = []
        
        # Lambdas for quick access
        g_deleted = lambda i: self.fvc.record[i]['diff']['global']['deleted']
        g_added = lambda i: self.fvc.record[i]['diff']['global']['added']
        g_changed = lambda i: self.fvc.record[i]['diff']['global']['changed']
        l_deleted = lambda i: self.fvc.record[i]['diff']['local']['deleted']
        l_added = lambda i: self.fvc.record[i]['diff']['local']['added']
        l_changed = lambda i: self.fvc.record[i]['diff']['local']['changed']
        
        i = 1 # Ignore 0th line (command from fvc)
        while i < len(fvc.record):
            
            # Case 1: function or class definition.
            # Pattern: line_no jumped forward
            if fvc.record[i]['line_no'] > fvc.record[i-1]['line_no']:
                # Check next lines of last executed line for [def] or [class]
                for target_line in range(fvc.record[i-1]['line_no'] + 1, fvc.record[i]['line_no']):    
                    for start, end, indentation, keyword in self.parser.code_blocks:
                        keyword_line = start - 1
                        if keyword_line == target_line and keyword in ("def", "class") and self.parser.indentations[keyword_line] == self.parser.indentations[fvc.record[i-1]['line_no']]:
                            actions.append((target_line, {keyword: self.parser.lines[start - 1]}))
            
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

                
            # Append actions
            if i == len(fvc.record) - 1 or fvc.record[i]['position'] in ("empty", "end"):
                actions.append((fvc.record[i]['line_no'], events))
            
            # Increment i
            i += 1
        return actions

if __name__ == "__main__":
    # Read filename from command line
    src_file = sys.argv[1]
    analyzer = SourceCodeAnalyzer(src_file)
    for action in analyzer.actions:
        input()
        print(action)
