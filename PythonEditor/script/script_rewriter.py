import re
import os

import script.find_variable_changes as fvc
import script.source_code_parser as scp

# TODO: triple quote is not considered

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
        # add a line 0
        self.lines.insert(1, fvc.first_line)

        # find code blocks
        codeblocks = self.parser.code_blocks
        print(codeblocks)

        # find code block starts (we cannot add commands there)
        codeblocks_starts = set([start for (start, end, indentation, keyword) in codeblocks])
        print(codeblocks_starts)

        # add the command
        is_empty_line = lambda line: bool(re.fullmatch("| *| *#.*", line))
        is_return_line = lambda line: bool(re.fullmatch("^ *return( *.*|\(*.*)$", line))
        for line_no_new, line in enumerate(self.lines):
            if line_no_new in (0, 1): # ignore index 0 (None) and 1 (first command from fvc)
                continue
            
            if line_no_new not in codeblocks_starts:
                line = line.splitlines()[0]
                if is_return_line(line):
                    indentation = self.parser.indentations[line_no_new - 1]
                    self.lines[line_no_new] = " " * indentation + fvc.command_return + line.lstrip() + "\n"
                elif not is_empty_line(line):
                    indentation = self.parser.indentations[line_no_new - 1]
                    self.lines[line_no_new] = " " * indentation + fvc.command_start + line.lstrip() + fvc.command_end + "\n"
                else:
                    # self.lines[line_no_new] = " " * self.parser.indentations[line_no_new - 1] + fvc.command_empty + "\n"
                    pass
        # Add the last line
        self.lines.append(fvc.last_line)

    def temp_file_name_generator(self, original_filename, name_func=lambda name: f"_{name}_temp.py"):
        return os.path.join(os.path.dirname(original_filename) ,name_func(os.path.basename(original_filename)))

    def _write_to_file(self, old_filename, name_func=lambda name: f"_{name}_temp.py"):
        new_name = self.temp_file_name_generator(old_filename, name_func) 
        with open(new_name, "w+", encoding="UTF-8") as file:
            file.writelines(self.lines[1:])
        return new_name

if __name__ == "__main__":
    target = "test2.py"
    sr = ScriptRewriter(target)
    sr.run()
