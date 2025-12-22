print("\n ======== abs ========") #절댓값 0에서부터의 거리

print(abs(3))
print(abs(-3))
print(abs(-0.2))



print("\n ======== all ========") # 반복 가능한 데이터를 받아서 요소가 모두 참이면 참

print(all([1,2,3])) # True
print(all([1,2,3,0])) # False
print(all((1,2,-1))) # True
print(all('파이썬 좋아요')) # 공백도 문자열 # True


print("\n ======== any =======")

print(any([1,2,0])) #요소들 중에 하나라도 참이면 참
print(any([0, ""]))



print("\n ======== chr / ord ========") # 유니코드 숫자를 

print(chr(97)) # a
print(chr(44032)) # 가

print(ord('a')) #97
print(ord('가')) #44032



print("\n ======== dir ========") # 객체가 지닌 변수나 함수를 반환

print(dir(([1,2,3])))
print(dir({'a':1}))



print("\n ======== divmod ========") # 몫과 나머지를 튜플로 반환

print(divmod(7,3))



print("\n ======== enumerate ========")

#(리스트, 튜플 등) 받아서 인덱스 포함하여 반환

for idx, name in enumerate(['body', 'foo', 'bar']):
    print(idx,name)



print("\n ======== eval ========") # 문자열을 실행

print(eval('1+2'))
print(eval("'hi' + 'hello'"))
print(eval('divmod(4,3)'))



print("\n ======== filter ========")

def positive(numbers):
    result = []
    for i in numbers:
        if i > 0:
            result.append(i)
    return result

numbers = [1, -3, 2, 0, -5, 6]

print(positive(numbers))

# filter(함수,반복가능한 데이터)
# 반환값이 참인 것만 반환

def positive(x):
    return x > 0

print(list(filter(positive, numbers)))

print(list(filter(lambda x: x > 0, numbers)))



print("\n ======== map ========")

numbers = [1, -3, 2, 0, -5, 6]

def two_times(numbers):
    result = []
    for i in numbers:
        result.append(i * 2)
    return result

a = two_times(numbers)
print(a)

# map(함수, 반복 가능 데이터)
# 요소별 결과 값 반환

def two_times(x):
    return x * 2

print(list(map(two_times, numbers)))

print(list(map(lambda x: x*2 , numbers)))