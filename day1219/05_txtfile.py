#(텍스트) 파일 읽고 쓰기

# r - 읽기모드
# w - 쓰기모드
# a - 추가모드 - 마지막에 새로운 내용추가


import os

path = './day1219'

if not os.path.exists(path):
    os.makedirs(path)


f = open("./day1219/새파일.txt",'w', encoding="utf-8")

for i in range(1,11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data) #메모장에 쓸 때는 문자열을 넣어야 한다.
f.close()

