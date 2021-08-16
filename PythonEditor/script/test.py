from pprint import pprint
from time import sleep

var_names = [i for i in locals().keys() if i[:2] != "__"]
for var_name in var_names:
    print(var_name, type(locals()[var_name]))

pprint(f"Hello world! Yo Yo Yo")
print("你好，世界😀")
def add(i, j):

    sum = i + j
    return sum

class CC:

    def __init__(self):
        self.name = "Cool!"
        self.age = "1000"
        self.description = "ooold"
        print(f"G:{globals().keys()}")
        print(f"L:{locals().keys()}")
        print(f"D:{dir(self)}")

    def scream(self):
        print(self.name)


li = []
for i in range(10):
    li.append(i)
    li.append(0)
print(li)

print(add(1,2))

if 10 == 10:
    print("Correct")
else:
    print("Incorrect")

cc = CC()



var_names = [i for i in locals().keys() if i[:2] != "__"]
for var_name in var_names:
    print(var_name, type(locals()[var_name]))

print(globals())