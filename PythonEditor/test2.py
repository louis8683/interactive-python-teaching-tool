import inspect
from pprint import pprint
from time import sleep

pprint(f"Hello world! Yo Yo Yo")
print("你好，世界！")

def add(i, j):
    sum = i + j
    return sum

class CC:
    def __init__(self):
        self.name = "Cool!"
        self.age = "1000"
        self.description = "ooold"
    
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

cc.scream()