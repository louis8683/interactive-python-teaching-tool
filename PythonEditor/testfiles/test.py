score = 10
answer = 6
guess = input("猜1-10的數字:")
while int(guess) != answer:
    score -= 1
    guess = input("猜錯了QQ 再猜一次:")
print(f"你的分數是 {score} 分")
p
