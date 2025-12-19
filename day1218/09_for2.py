# 각 요소에 3 곱하기

a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num*3)

print(result)  # [3, 6, 9, 12]




print('\n======= 리스트 컴프리헨션 =======')

# 각 요소에 3 곱하기

a = [1, 2, 3, 4]

result = [num * 3 for num in a]

print(result) # [3, 6, 9, 12]
print()






# 짝수에만 3 곱하기

a = [1, 2, 3, 4]

result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]
print()

# [결과 for 항목 in 리스트(튜플) if 문 ]
# for문을 2개 이상 사용하는 것도 가능 하다.




result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)




print("\n======= break =======\n")

for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
print()

print("안녕히 주무세요")




print("\n======= for-else 문 =======\n") # for문이 정상종료 되었을때만 else문 작동


for i in range(5):
    print(i)
else:
    print("for문 정상종료.")

print()



for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for문 정상종료???")






print("\n======= enumerate 함수 =======\n")


fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

print()




for i, fruit in enumerate(fruits, 1):  # 1부터 시작
    print(f'{i}: {fruit}')

print()



print("\n======= zip 함수 =======\n")


names = ['홍길동', '김철수', '이영희']
scores = [85, 93, 56]


a = zip(names, scores)
print('\na 출력')
print(a)



print('\nlist(a) 첫번째 출력')
print(list(a))

print('\nlist(a) 두번째 출력')
print(list(a))

print()



names = ['홍길동', '김철수', '이영희']
scores = [85, 93, 56]

# [('홍길동', 85), ('김철수', 93), ('이영희', 56)]
for name, score in zip(names, scores):
    print(f'{name}: {score}점')

print()



print('\n======= 개수가 안맞는 경우 =======\n')

names = ['홍길동', '김철수', '이영희', '박영수']
scores = [85, 93, 56]

for name, score in zip(names, scores): # 개수가 안맞을 경우 무시됨.
    print(f'{name}: {score}점')

print()




print('\n======= zip_longest =======\n')

# zip_longest 임포트!
from itertools import zip_longest

for name, score in zip_longest(names, scores, fillvalue="점수 없음"): 
    print(f'{name}: {score}')

print()




print('\n======= zip 실습 =======')

names = ['홍길동', '김철수', '이영희']
korean = [85, 93, 56]
english = [90, 100, 95]

# 홍길동 : 국어 85점, 영어 90점




for i in range(1,5):
    print(" " * (5-i) + '*' * (i*2 -1))


    print("\n")


height = 5
width = 2 * height - 1

for i in range(height):
    stars = '*' * (2*i + 1)
    print(f'{stars:^{width}}')


print("\n")



height = 5

for i in range(height):
    stars = '*' * (2*i + 1)
    print(stars.center(9))


print("\n")


height = 5

for i in range(-(height-1), height):
    spaces = abs(i)
    stars = 2 * (height - spaces) - 1

    print(' ' * spaces + '*' * stars)


print("\n")


for a in range(1,10):
    b = abs(a-5)
    c = abs(b-5)*2 -1


    print(' ' * b + '*' * c)


print("\n")

arr = [5,3,8,1,2]
n = len(arr) # 5

for i in range (n-1): # 4라운드 마다 진행 0 1 2 3
    for j in range (0, n - i - 1): #라운드마다 4 3 2 1번
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


arr = [5,3,8,1,2]
n = len(arr)

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)