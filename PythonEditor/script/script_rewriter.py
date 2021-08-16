import find_variable_changes as fvc
from find_code_blocks import find_code_blocks, indentation_from_codeblocks
import re

class ScriptRewriter:
    def __init__(self, sript_filename: str):
        self.lines: list[str] = [None] # use an empty index 0 to match the line number with index
        self.src_filename = sript_filename

    def run(self):
        self._read_script()
        self._add_commands()
        self._write_to_file(self.src_filename)
    
    def _read_script(self):
        # read in a target python sript
        with open(self.src_filename, "r", encoding="UTF-8") as file:
            for line in file:
                self.lines.append(line)

    def _add_commands(self):
        # add a line 0
        self.lines.insert(1, fvc.first_line)

        # find code blocks
        codeblocks = find_code_blocks(self.lines)
        print(codeblocks)

        # find code block starts (we cannot add commands there)
        codeblocks_starts = set([start for (start, end) in codeblocks])

        # add the command
        is_empty_line = lambda line: bool(re.fullmatch("| *| *#.*", line))
        for line_no, line in enumerate(self.lines):
            if line_no in (0, 1): # ignore index 0 (None) and 1 (first command from fvc)
                continue
            
            if line_no not in codeblocks_starts:
                line = line.splitlines()[0]
                if not is_empty_line(line):
                    indentation = indentation_from_codeblocks(codeblocks, line_no, self.lines)
                    self.lines[line_no] = " " * indentation + fvc.command_start + line.lstrip() + fvc.command_end + "\n"
                else:
                    self.lines[line_no] = " " * indentation_from_codeblocks(codeblocks, line_no, self.lines) + fvc.command_empty + "\n"
        # Add the last line
        self.lines.append(fvc.last_line)

    def _write_to_file(self, old_filename, name_func=lambda name: f"_{name}_temp.py"):
        with open(name_func(old_filename), "w+", encoding="UTF-8") as file:
            file.writelines(self.lines[1:])

if __name__ == "__main__":
    target = "test2.py"
    sr = ScriptRewriter(target)
    sr.run()
