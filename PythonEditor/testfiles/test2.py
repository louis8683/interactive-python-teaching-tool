1 == 0
score = 10
answer = 6
guess = input("猜1-10的數字:")
while int(guess) != answer:
    score -= 1
    guess = input("猜錯了QQ 再猜一次:")
print(f"你的分數是 {score} 分")

def add(x, y):
    sum = x + y
    print(sum)
    return sum

a, b = 10, 12
add(a, b)