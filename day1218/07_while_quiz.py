# 1부터 100까지 합 구하기

total = 0
num = 1

while num <= 100:
    total += num
    num += 1

print(total)



# 1~100 숫자 중에 3의 배수만 출력하기

num = 1

while num <= 100:
    if num % 3 == 0:
        print(num)
    num += 1



# 숫자 맞추기 게임
# 숫자 맞추기는 컴퓨터가 랜덤으로 생성한 숫자를 사용자가  input 으로 숫자 넣으면서 맞춰보는 것

import random

answer = random.randint(1, 100)
guess = 0

while guess != answer:
    guess = int(input("(1~100): "))

    if guess > answer:
        print("다운")
    elif guess < answer:
        print("업")
    else:
        print("정답")


# 구구단 출력

dan = 2

while dan <= 9:
    num = 1
    print(f"\n{dan}단")

    while num <= 9:
        print(f"{dan} x {num} = {dan * num}")
        num += 1
    dan += 1
      
