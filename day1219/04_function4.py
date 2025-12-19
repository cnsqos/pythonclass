print('\n======= 람다식 =======')

#함수를 간단하게 만들기

def add(a,b):
    return a+b

add2 = lambda a, b: a+b

result = add2(3,4)
print(result)
print()




print('\n======= 리스트 + 맵 =======')

numbers = [1,2,3,4,5]
squares =  list(map(lambda x:x**2, numbers))
print(squares)
print()



print('\n======= 리스트 컴프리헨션=======')

squares2 = [x**2 for x in numbers]


print('\n======= 리스트 + 필터 =======')

numbers2 = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x : x %2 ==0, numbers2))
print(evens)
print()


#리스트 컴프리헨션 방식으로 똑같은 작동 구현하기

evens2 = [x**2 for x in numbers2 if x % 2 ==0]
print(evens2)



print("\n======= 예제1 ========")

numbers3 = [5,-2,0,8,-7]
result = list(map(lambda x : "양수" if x>0 else ("음수" if x < 0 else "0"), numbers3))
print(result)
print()


#리스트 컴프리헨션 방식으로 똑같은 작동 구현하기

result2 = ["양수" if x>0 else ("음수" if x < 0 else "0") for x in numbers3]
print(result2)


print("\n======= 예제2 ========")

a = [1, 2, 3, 4]

result = [num * 3 for num in a if num % 2 == 0]
print(result)
print()
