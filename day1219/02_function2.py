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

