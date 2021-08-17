# import modules
import re
from types import LambdaType

codeblock_keywords = {"if", "elif", "else", "while", "for", "def", "class", "try", "except", "else", "finally"}


class SourceCodeParser:
    def __init__(self, filename="", encoding="UTF-8", line_no_start=1):
        self.offset = line_no_start
        if filename:
            self.load_file(filename, encoding)
    
    def load_file(self, filename, encoding="UTF-8"):
        self.lines: list[str] = [""] * self.offset # match the index with the line_no
        with open(filename, "r", encoding=encoding) as file:
            for line in file:
                self.lines.append(line)
        self._parse()
    
    def _parse(self):
        self.indentations = self.find_indentations(self.lines, self.offset)
        self.code_blocks = self.find_code_blocks(self.indentations, self.offset)

    def find_indentations(self, lines, offset) -> list[int]:
        indentations = [0] * offset
        keywords_regex = self.concat_keywords_regex(codeblock_keywords, keyword_modifier=lambda keyword: keyword + " ")
        # form patterns
        valid_block_start_pattern = f"^ *{keywords_regex}[^#|:]*: *(#.*)?$"
        empty_line_pattern = f"^ *(#.*)?$"
        # loop over lines
        for i, line in enumerate(lines[self.offset:]):
            indentation = re.match(" *", line).span()[1] 

            # Case 1: empty line or pure comment
            if re.match(empty_line_pattern, line):
                indentations.append(-1) # append a special token for later update
            # Case 2: other statements and not comment
            else:
                indentations.append(indentation)

        indentations += [0] # append a 0 to mark indentation of last line
        # reverse loop over indentation to change tokens into numbers
        for i in reversed(range(len(indentations))):
            if indentations[i] == -1:
                indentations[i] = indentations[i+1]
        return indentations[:-1] # remove last one used for token replacing
            
    def concat_keywords_regex(self, keywords: list[str]=codeblock_keywords, keyword_modifier: LambdaType=lambda keyword: keyword) -> str:
        if len(keywords) == 0:
            return ""
        expression = "("
        for keyword in keywords:
            expression += keyword_modifier(keyword) + "|"
        return expression[:-1] + ")"

    def find_code_blocks(self, indentations: list[int], offset) -> list[tuple[int,int,int]]:
        # use a stack to find all the code blocks
        stack = []
        code_blocks:list[tuple(int,int,int,str)] = [] # (start,end,indentation,keyword)
        keywords_regex = self.concat_keywords_regex() # for searching keywords
        
        line_no = offset
        indentations += [0] # To find code block at end
        while line_no <= len(indentations[offset:]):
            indentation = indentations[line_no]
            if indentation > 0 and (len(stack) == 0 or indentation > stack[-1][0]):
                stack.append((indentation, line_no))
            elif indentation >= 0 and stack and indentation < stack[-1][0]:
                popped = stack.pop()
                match: re.Match = re.search(f"{keywords_regex}(?= |:|)", self.lines[popped[1] - 1])
                code_blocks.append((popped[1], line_no - 1, popped[0], self.lines[popped[1] - 1][match.span()[0]:match.span()[1]]))
                continue # skip the increment of line_no
            elif indentation < 0:
                raise ValueError("Indentation cannot be negative")
            line_no += 1
        return code_blocks

if __name__ == "__main__":
    
    target_file = "test2.py"
    scp = SourceCodeParser(target_file)
    print(scp.indentations)
    print(scp.code_blocks)
