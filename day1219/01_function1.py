print('\n======= 함수 =======\n')

def add(a, b):
    return a + b

hap = add(3, 4)
print(hap)

c = 5
d = 6

hap = add(c, d)
print(hap)


print('\n======= 입력값, 반환값 있는 경우 =======\n')

#조금 더 정석적으로 표현

def add(a,b):
    result = a + b # a,b 는 매개변수 (parameter)
    return result

hap = add(4,7) # 4,7 은 인수(arguments)
print (hap)


print('\n======= 입력값이 없는 함수 =======\n')

def say():
    return 'hi'

say() # 아무것도 안나옴

a = say()
print(a) #hi


print('\n======= 입력값, 반환값 없는 함수 =======\n')


def say2():
    print("hi")


say2()

a = say2()
print(a)
print(say2())


print('\n======= 입력값만 있는 경우 =======\n')

def add2(a,b):
    print(f'{a}와 {b}의 합은 {a+b} 입니다')
    return a+b

a = add2(3,4)

print(a)


print('\n======= 혼합하기 =======\n')


def add2(a,b):
    print(f'{a}와 {b}의 합은 {a+b} 입니다')
    print(f'하지만 반환하는 값은 {a} x {b} 입니다')
    result = a * b
    return result

a = add2(3,4)

print(a)


print('\n======= 매개변수 지정하여 입력 =======\n')

def sub(a,b):
    return a - b

result = sub(a=3, b=4)
print(result)


result = sub(b=5,a=9) #매개변수 지정하면 순서 달라도 된다.
print(result)



# 4가지 경우 만들어보세요
# 입력값 o x 반환값 o x

