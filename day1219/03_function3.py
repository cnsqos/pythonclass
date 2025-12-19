#함수의 반환값은 언제나 하나이다.

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)#(7,12)
print(result)
print()

result1,result2 = add_and_mul(5,6)
print(result1)
print(result2)
print()


print("\n====== return의 또다른 쓰임새 ======\n")

def say_nick(nick):
    if nick == "바보":
        return
    print(f'나의 별명은 {nick} 입니다.')

say_nick('바보') #반응 안함
say_nick('천재')


print("\n====== 매개변수 미리 지정 ======\n")

def say_myself(name, age, man = True):
    print(f"나의 이름은 {name} 입니다.")
    print(f"나이는 {age}살 입니다.")
    if man : print("남자입니다.")
    else: print("여자입니다.")

say_myself('김둘리', 3)
print()

say_myself('김둘리', 3, True)
print()

say_myself('이또치', 4, False)
print()


print("\n====== 지역변수(local), 전역변수(global) ======\n")

a = 3

def exam(number):
    a = 0
    a = a + number

exam(5)
print(a)

print("\n======== 반환값으로 받기 =============\n")

a=3

def exxam(number):
    a=0
    a=a+number
    return a

print(exam(5))
print(a)


print("\n========  global 명령어 사용 ===========\n")

a = 3

def exam(number):
    global a

    a= a + number

exam(5)
print(a)


print("\n======== 리스트나 딕셔너리 함수에서 변경가능 ===========\n")


def chage_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
chage_list(a)

print(a)


def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float) : 첫 번째 숫자
    b (int, float) : 두 번째 숫자

    Returns:
    int, float : 두 숫자의 합
    """
    return a + b

print (add.__doc__)