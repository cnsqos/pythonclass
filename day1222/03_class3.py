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

d = FourCal(4,2)
print(d.add())
print(d.div())

