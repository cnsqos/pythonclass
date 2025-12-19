# 여러개의 입력값을 받는 함수
# 몇개를 받을지 정해지지 않았을 때

print('\n======= 여러개의 인수를 받는 경우 =======\n')

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

sum = add_many(1,2,3)
print(sum) #6
print()


sum = add_many(2,3,11,17,23,29,34)
print(sum)
print()




def add_mul(choice,*args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result *i

    else:
        result = '그런 연산은 없습니다'

    return result

result = add_mul('add', 1,2,3)
print(result)

result = add_mul('mul', 1,2,3)
print(result)


print('\n======= 키:밸류를 인수로 받는 경우 =======\n')

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print()

print_kwargs(name='poo', age=3)
print()

print_kwargs(name='홍길동', age = 25, city='서울', job='정의로운 도둑')
print()


def create_profile(**info):
    print("===== 프로필 정보 =====")
    for key, value in info.items():
        print(f'{key}: {value}')

create_profile(이름='김철수', 나이=30, 직업='개발자', 취미='독서')
print()


print('\n======= 3가지 형식을 인수로 받는 경우 =======\n')


def mixed_profile(name, *args, **kwargs):
    print(f'이름: {name}')
    print(f'좋아하는 숫자: {args}')
    print(f'기타 정보: {kwargs}')

mixed_profile('홍길동', 3, 7, 9, age=17, city='서울')
print()


name = '번개맨'
fav_number = [3,7,9]
extra_info = {'age':15,'city':'인천'}

def mixed_profile(name, *args, **kwargs):
    print(f'이름: {name}')
    print(f'좋아하는 숫자: {args}')
    print(f'=== 기타 정보 ===')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

mixed_profile(name, *fav_number, **extra_info)
print()