# Let's write a simple recursion
def deep_add(obj:list):
    # End condition, return 0 if empty
    if len(obj) == 0:
        return 0
    
    # This is a recursive deep add function
    sum = 0
    for element in obj:
        if type(element) in (tuple, list):
            sum += deep_add(element)
        elif type(element) in (int, float):
            sum += element
    
    # Return sum
    return sum

deep_list = [[1,1],1,1]
answer = deep_add(deep_list)
print(answer)
print("Hello")
print("World")
print("!!")