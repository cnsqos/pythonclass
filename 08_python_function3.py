print("\n ======== pow ========")

print(pow(2, 4)) #16
print(pow(2, 100))


print("\n ======== range ========")

print(list(range(5)))
print(list(range(5,10)))

print(list(range(1,10,2)))

print(list(range(0,-11,-2)))
print(list(range(0,-11,-1)))



print("\n ======== round ========")

print(round(4.6)) #5
print(round(4.2)) #4
print(round(4.5)) #4
print(round(4.51)) #5
print(round(5.5)) #6

#가까운 짝수쪽으로 붙음

print(round(5.678, 2)) # 5.68


print("\n ======== sorted ========")

print(sorted([3,1,2])) #[1,2,3]
print(sorted(['a','c','b']))
print(sorted('zero'))


print("\n ======== str ========") # 문자열로 반환

print(str(3))
print(str('hi'))


print("\n ======== sum ========")

print(sum([1,2,3])) #6
print(sum((4,5,6))) #15

print("\n ======== tuple ========") # 반

print(tuple('abc'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

print("\n ======== type ========")

print(type('abc'))
print(type([]))
print(type((open('test','w'))))
#<class '_io.TextIOWrapper'> 텍스트 기반 입출력 객체

print("\n ======== zip ========")

print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip('abc', 'def')))

