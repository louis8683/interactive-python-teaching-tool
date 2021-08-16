import inspect
print(f"lineno: {inspect.currentframe().f_lineno}");from pprint import pprint;print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");from time import sleep;print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");pprint(f"Hello world! Yo Yo Yo");print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");print("你好，世界😀");print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
def add(i, j):
    print(f"lineno: {inspect.currentframe().f_lineno}");sum = i + j;print(f"lineno: {inspect.currentframe().f_lineno}")
    print(f"lineno: {inspect.currentframe().f_lineno}");return sum
print(f"lineno: {inspect.currentframe().f_lineno}")
class CC:
    def __init__(self):
        print(f"lineno: {inspect.currentframe().f_lineno}");self.name = "Cool!";print(f"lineno: {inspect.currentframe().f_lineno}")
        print(f"lineno: {inspect.currentframe().f_lineno}");self.age = "1000";print(f"lineno: {inspect.currentframe().f_lineno}")
        print(f"lineno: {inspect.currentframe().f_lineno}");self.description = "ooold";print(f"lineno: {inspect.currentframe().f_lineno}")
    print(f"lineno: {inspect.currentframe().f_lineno}")
    def scream(self):
        print(f"lineno: {inspect.currentframe().f_lineno}");print(self.name);print(f"lineno: {inspect.currentframe().f_lineno}")
    print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");li = [];print(f"lineno: {inspect.currentframe().f_lineno}")
for i in range(10):
    print(f"lineno: {inspect.currentframe().f_lineno}");li.append(i);print(f"lineno: {inspect.currentframe().f_lineno}")
    print(f"lineno: {inspect.currentframe().f_lineno}");li.append(0);print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");print(li);print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");print(add(1,2));print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
if 10 == 10:
    print(f"lineno: {inspect.currentframe().f_lineno}");print("Correct");print(f"lineno: {inspect.currentframe().f_lineno}")
else:
    print(f"lineno: {inspect.currentframe().f_lineno}");print("Incorrect");print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");cc = CC();print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}")
print(f"lineno: {inspect.currentframe().f_lineno}");cc.scream();print(f"lineno: {inspect.currentframe().f_lineno}")