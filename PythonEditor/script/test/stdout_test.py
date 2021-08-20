import sys
import io
from typing import Iterable
from pprint import pprint

org_stdout = sys.stdout

class CustomStdout(io.TextIOBase):
    def __init__(self):
        super().__init__()
        self.history = []
        self.log = []
    
    def write(self, __s: str) -> int:
        self.history.append(__s)
        self.log.append({"write": __s})
        return len(__s)
    
    def writelines(self, __lines: Iterable[str]) -> None:
        self.log.append({"writelines": __lines})
        for line in __lines:
            self.write(line)

class CustomStdin(io.TextIOBase):
    def __init__(self, input_list: Iterable[str]) -> None:
        super().__init__()
        self.input_list = input_list
        self.counter = 0
    
    def read(self, *args) -> str:
        val = self.input_list[self.counter]
        self.counter += 1
        return val
    
    def readline(self, *args) -> str:
        return self.read()
    
    def readlines(self, __hint: int) -> list[str]:
        return self.input_list[self.counter:]

class CustomStderr(io.TextIOBase):
    def __init__(self) -> None:
        super().__init__()
        self.history = []
        self.log = []
    
    def write(self, __s: str) -> int:
        print(f"write error: {__s}")
        print("".join(self.history))
        self.history.append(__s)
        self.log.append({"write": __s})
        return len(__s)
    
    def writelines(self, __lines: Iterable[str]) -> None:
        print(f"writelines error: {__lines}")
        self.log.append({"writelines": __lines})
        for line in __lines:
            self.write(line)

custom_stdout = CustomStdout()
sys.stdout = custom_stdout

print("Hi, how are you?")
pprint([[1,2,3],[1,2,3],[1,2,3]])

sys.stdout = org_stdout
print(custom_stdout.history)
print(custom_stdout.log)
for history in custom_stdout.history:
    print(history, end="")

input_list = ["Hello world"]
custom_stdin = CustomStdin(input_list)
org_stdin = sys.stdin
sys.stdin = custom_stdin

i = input()
print(i)

custom_stderr = CustomStderr()
org_stderr = sys.stderr
sys.stderr = custom_stderr

1 / 0
print(custom_stderr.history)
