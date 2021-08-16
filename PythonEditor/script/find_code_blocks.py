'''
This program finds all the code blocks of the input python file.
'''

# import modules

import re

# keywords: condition{if, elif, else} loop{while, for} func{def} class{class}
#           error{try, except, else, finally} file{with}
keywords = {"if", "elif", "else", "while", "for", "def", "class", "try", "except", "else", "finally"}

def find_code_blocks(lines: list, ignore_zeroth_line=True, keywords: set=keywords) -> list[tuple[int, int]]:
    ''' This function returns the list of all the code blocks of the input list of lines of code.
    The return format is of list[tuple(start, end)]
    Note: this function ignores the 0th line to match the line number of the Python interpreter.
    '''
    
    # Create RE pattern for keyword detection
    re_pattern = ""
    for keyword in keywords:
        re_pattern += f" *{keyword}.*|"
    re_pattern = re_pattern[:-1] # remove trailing "|"
    # TODO: remove one liner with re
    print(re_pattern)

    # Variable setup
    codeblocks = []
    codeblock_incomplete_stack = []
    indentation, last_indentation = 0, 0

    # Lambda functions for more readable code
    is_empty_line = lambda line: bool(re.fullmatch("| *| *#.*", line.splitlines()[0]))
    is_keyword_line = lambda line: re.match(re_pattern, line) is not None

    print("LOOP")
    # Loop: go through each line
    for line_no, line in enumerate(lines + ["\n"]): # add a empty last line to clean up incomplete codeblocks
        if ignore_zeroth_line and line_no == 0: # ignore first line (to match line_no)
            lines[0] = "\n" # So the last line of indentation finding won't run into error
            continue
        
        # Indentation
        if line_no == len(lines): # last dummy line, cleanup
            indentation = 0
        elif is_keyword_line(lines[line_no - 1]) is not None and is_empty_line(line): # last line is start of code block and this line is empty
            indentation += 4 # This number is temporary, new lines
        elif is_empty_line(line): # empty line
            pass # don't change indentation
        else: # use current indentation
            indentation = re.match(" *", line).span()[1]    

        # Detect start and end of code blocks
        if indentation < last_indentation: # end of some code blocks, ignore empty lines
            while codeblock_incomplete_stack and codeblock_incomplete_stack[-1][1] > indentation:
                codeblocks.append((codeblock_incomplete_stack.pop()[0], line_no - 1))

        if re.match(re_pattern, line) is not None: # found a start of a code block
            codeblock_incomplete_stack.append((line_no, indentation + 4))
        
        # Update last_indentation
        last_indentation = indentation
    return codeblocks

def find_code_blocks_with_file(filename, encoding="UTF-8", keywords=keywords):
    ''' This is basically a wrapper for find_code_blocks() that simplifies file I/O.'''
    # read in the target file into list of lines
    lines = [""] # use an empty index 0 to match the line number with index
    with open(filename, "r", encoding=encoding) as file:
        for line in file:
            lines.append(line)
    return find_code_blocks(lines, keywords=keywords)

def indentation_from_codeblocks(codeblocks: list[tuple[int, int]], line_no: int, lines: list):
    codeblocks.sort()
    max_indentation = 0
    for i, (start, end) in enumerate(codeblocks):
        if start < line_no <= end and re.match(" *", lines[start]).span()[1] + 4 > max_indentation :
            max_indentation = re.match(" *", lines[start]).span()[1] + 4
    return max_indentation            

if __name__ == "__main__":
    
    target_file = "test2.py"
    codeblocks = find_code_blocks_with_file(target_file)
    print(f"Code block starts: {codeblocks}")
