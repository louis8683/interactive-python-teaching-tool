from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat
from copy import deepcopy


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, doc):
        super().__init__(doc)
        
        # Keywords

        self.all_keywords = set(['False', 'None', 'True', 'and', 'as', 'assert',
            'async', 'await', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
            'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
            'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'])

        # Colored in magenta, same as VS code
        self.magenta_keywords = set(['and', 'as', 'assert',
            'async', 'await', 'break', 'class', 'continue', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
            'if', 'import', 'nonlocal',
            'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'])

        # Colored in blue
        self.blue_keywords = self.all_keywords - self.magenta_keywords

        # Capital
        self.capital_keywords = set(['False', 'None', 'True'])

        # Types, reference: https://docs.python.org/3/library/stdtypes.html#context-manager-types
        # Colored in cyan
        self.type_keywords = set(["int", "float", "complex", 
            "str", 
            "range", "list", "tuple", 
            "dict", "set", "frozenset",  
            "bytes", "bytearray", "memoryview",
            "type", "bool"])
        
        # Functions

        # Builtin functions, src(Python): import builtins; dir(builtins)
        self.builtin_functions = set(['__build_class__', '__debug__', '__doc__', 
            '__import__', '__loader__', '__name__', '__package__', '__spec__', 
            'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 
            'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 
            'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 
            'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 
            'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 
            'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 
            'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 
            'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
            'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 
            'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'])
        self.yellow_builtin_functions = self.builtin_functions - self.type_keywords
    
    def base_format(self, bold=True):
        format = QTextCharFormat()
        if bold:
            format.setFontWeight(QFont.Bold)
        else:
            format.setFontWeight(QFont.Normal)
        format.setFontFamily("Consolas")
        format.setForeground(Qt.black)
        return format
        
    def highlightBlock(self, text):
        
        # Set base format
        self.setFormat(0, len(text), self.base_format(bold=False))

        # Keywords
        
        # Dark magenta
        for keyword in self.magenta_keywords:
            self.highlight_keyword(text, keyword, Qt.darkMagenta)
        # Blue
        for keyword in self.blue_keywords:
            self.highlight_keyword(text, keyword, Qt.blue)
        # Cyan
        for keyword in self.type_keywords:
            self.highlight_keyword(text, keyword, Qt.darkCyan)

        # Builtin Functions
        for keyword in self.yellow_builtin_functions:
            self.highlight_function(text, keyword)
        
        # Decorators
        self.highlight_decorator(text)
        
        # Strings
        self.highlight_string(text)
        
        # Comments, NOTE: This has to be the last
        self.highlight_comment(text)
        
    def highlight_keyword(self, text, keyword, color):
        self.highlight(text, color, f"^{keyword}+[^a-zA-Z0-9._]|[^a-zA-Z0-9._]+{keyword}+[^a-zA-Z0-9._]|^{keyword}$|[^a-zA-Z0-9._]+{keyword}$")

    def highlight_comment(self, text, color=Qt.green):
        self.highlight(text, color, f"#.*")
    
    def highlight_function(self, text, keyword, color=Qt.darkYellow):
        self.highlight(text, color, f"^{keyword}+[\(]|[^a-zA-Z0-9._]+{keyword}+[\(]", highlight_offset=(0,-1))
    
    def highlight_decorator(self, text, color=Qt.darkYellow):
        self.highlight(text, color, "^@[a-zA-Z0-9._]*| @[a-zA-Z0-9._]*")
    
    def highlight_string(self, text, color=Qt.darkRed, f_color=Qt.blue):
        format = self.base_format()
        format.setForeground(color)
        f_format = self.base_format()
        f_format.setForeground(f_color)
        double_quote_pos = []
        single_quote_pos = []
        for i, c in enumerate(text):
            if c == "'":
                single_quote_pos.append(i)
            elif c == '"':
                double_quote_pos.append(i)
        # Recursive find all valid pairs
        pairs = self._find_all_pairs(double_quote_pos, single_quote_pos)
        for pair in pairs:
            # Find f-strings
            curly_pair = []
            if pair[0] > 0 and ((pair[0]==1 and text[0] == "f") or (pair[0] > 1 and QRegularExpression("[^a-zA-Z0-9._]+f").globalMatch(text[pair[0]-2:pair[0]]).hasNext())):
                # highlight the f
                self.setFormat(pair[0]-1, 1, f_format)
                # find the curly brackets
                curly_head, curly_tail = [], []
                for i, c in enumerate(text[pair[0]:pair[1]]):
                    if c == "{":
                        curly_head.append(pair[0] + i)
                    elif c == "}":
                        curly_tail.append(pair[0] + i)
                # match the braces
                for pos in curly_head:
                    if curly_tail:
                        curly_pair.append((pos, curly_tail[0]))
                        del curly_tail[0]

            # find the intervals skipping the curly braces
            intervals = []
            current_start = pair[0]
            for start, end in curly_pair:
                intervals.append((current_start, start))
                current_start = end
            intervals.append((current_start, pair[1]))

            # set format of string
            for start, end in intervals:
                self.setFormat(start, end - start + 1, format)
    
    def _find_all_pairs(self, double_quote_pos, single_quote_pos) -> list[list[int, int]]:
        '''Recursively find all valid string quote pairs'''
        # end condition: neither len is enough
        if len(double_quote_pos) < 2 and len(single_quote_pos) < 2:
            return []
        
        # Extract first pair
        double = double_quote_pos[:2] if len(double_quote_pos) >= 2 else None
        single = single_quote_pos[:2] if len(single_quote_pos) >= 2 else None
        # Find valid pair
        if double is None and single is not None: # Double is empty
            return [single] + self._find_all_pairs(double_quote_pos, single_quote_pos[2:])
        elif double is not None and single is None: # Single is empty
            return [double] + self._find_all_pairs(double_quote_pos[2:], single_quote_pos)
        else:
            if single is None or double[0] < single[0]: # Double is chosen
                # remove every single position before end of double
                while single_quote_pos and single_quote_pos[0] < double[1]:
                    del single_quote_pos[0]
                # recursion
                return [double] + self._find_all_pairs(double_quote_pos[2:], single_quote_pos)
            elif double is None or double[0] > single[0]: # Single is chosen
                # remove every double position before end of double
                while double_quote_pos and double_quote_pos[0] < single[1]:
                    del double_quote_pos[0]
                # recursion
                return [single] + self._find_all_pairs(double_quote_pos, single_quote_pos[2:])
            else: # Equal is impossible
                raise IndexError("Double and single quote have same position.")



    def highlight(self, text, color, regex, highlight_offset=(0,0)):
        format = self.base_format()
        format.setForeground(color)
        expression = QRegularExpression(regex)
        matches = expression.globalMatch(text)
        while matches.hasNext():
            match = matches.next()
            self.setFormat(match.capturedStart() + highlight_offset[0], match.capturedLength() + highlight_offset[1], format)      
