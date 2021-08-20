import re
import os

import script.find_variable_changes as fvc
import script.source_code_parser as scp

# TODO: triple quote is not considered ('''something something...''')
# TODO: line break is not considered (\)

class ScriptRewriter:
    def __init__(self, sript_filename: str):
        self.lines: list[str] = [None] # use an empty index 0 to match the line number with index
        self.src_filename = sript_filename
        # init Source Code Parser
        self.parser = scp.SourceCodeParser(self.src_filename)

    def run(self):
        self._read_script()
        self._add_commands()
        self.generated_filename = self._write_to_file(self.src_filename)
    
    def _read_script(self):
        # read in a target python sript
        with open(self.src_filename, "r", encoding="UTF-8") as file:
            for line in file:
                self.lines.append(line)

    def _add_commands(self):
        # insert leading commands of fvc into lines from index 1
        self.lines = self.lines[0:1] + fvc.first_lines + self.lines[1:]

        # find code blocks
        codeblocks = self.parser.code_blocks

        # find code block starts (we cannot add commands there)
        codeblocks_starts = set([start + len(fvc.first_lines) - 1 for start, _, _, _ in codeblocks])

        # add the command
        is_empty_line = lambda line: bool(re.fullmatch("| *| *#.*", line))
        is_return_line = lambda line: bool(re.fullmatch("^ *return( *.*|\(*.*)$", line))
        for line_no_new, line in enumerate(self.lines):
            if line_no_new <= len(fvc.first_lines): # ignore index 0 (None) and first commands from fvc
                continue
            
            
            
            # Add commands
            if line_no_new not in codeblocks_starts:
                line = line.splitlines()[0] # remove newline
                if is_return_line(line):
                    indentation = self.parser.indentations[line_no_new - len(fvc.first_lines)]
                    self.lines[line_no_new] = fvc.leading_spaces + " " * indentation + fvc.command_return + line.lstrip() + "\n"
                elif not is_empty_line(line):
                    indentation = self.parser.indentations[line_no_new - len(fvc.first_lines)]
                    self.lines[line_no_new] = fvc.leading_spaces + " " * indentation + fvc.command_start + line.lstrip() + fvc.command_end + "\n"
                else:
                    # Add the leading spaces from fvc
                    self.lines[line_no_new] = fvc.leading_spaces + self.lines[line_no_new]
            else:
                # Add the leading spaces from fvc
                self.lines[line_no_new] = fvc.leading_spaces + self.lines[line_no_new]
        
        # Add the last lines
        self.lines += fvc.last_lines

    def temp_file_name_generator(self, original_filename, name_func=lambda name: f"_{name}_temp.py"):
        return os.path.join(os.getcwd() ,name_func(os.path.basename(original_filename)))

    def _write_to_file(self, old_filename, name_func=lambda name: f"_{name}_temp.py"):
        new_name = self.temp_file_name_generator(old_filename, name_func) 
        with open(new_name, "w+", encoding="UTF-8") as file:
            file.writelines(self.lines[1:])
        return new_name
