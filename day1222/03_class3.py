# 사칙연산 클래스

'''
a = FourCal()

a.setdata(4,2)

a.add() >>> 6
a.mul() >>> 8
a.sub() >>> 2
a.div() >>> 2
'''

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second


    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


# a = FourCal()
# print(type (a))

# a.setdata(4,2)

# print(a.first)
# print(a.second)
# print()


# b = FourCal()

# b.setdata(3,5)
# print(b.first)
# print(a.first)
# print()


# print("a.add():" , a.add())
# print("a.add():" , a.mul())
# print("a.add():" , a.sub())
# print("a.add():" , a.div())

# c = FourCal()
# print(c.add())

# d = FourCal(4,2)
# print(d.add())
# print(d.div())



print('\n======== 클래스 상속 ========\n')

class MoreFourCal(FourCal):

    # # third = 777 # 클래스 변수

    def pow(self):
        return self.first ** self.second

    # div 메서드 오버라이딩

    def div(self):
        if self.second == 0: #나누는 값이 0인 경우 0을 리턴
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4, 2)

print("add :", a.add())
print("sub :", a.sub())
print("mul :", a.mul())
print("div :", a.div())
print("pow :", a.pow())




b = MoreFourCal(4, 0)
print(b.div()) # 메서드 오버라이딩 한 후에는 에러 안뜬다.

