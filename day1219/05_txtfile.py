#(텍스트) 파일 읽고 쓰기

# r - 읽기모드
# w - 쓰기모드
# a - 추가모드 - 마지막에 새로운 내용추가


import os

path = './day1219'

if not os.path.exists(path):
    os.makedirs(path)


# f = open("./day1219/새파일.txt",'w', encoding="utf-8")

# for i in range(1,11):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data) #메모장에 쓸 때는 문자열을 넣어야 한다.
# f.close()



# print("\n======== 읽기 모드 (readline) ========\n")

# f = open("./day1219/새파일.txt",'r',encoding="utf-8")
# line = f.readline() # 첫 번째 출을 반환
# print(line)
# f.close()




# print("\n======== while 문으로 여러줄 읽기 ========\n")

# f = open("./day1219/새파일.txt",'r',encoding="utf-8")
# while True:
#     line = f.readline() # 첫 번째 출을 반환
#     if not line: break
#     print(line)
# f.close()



# print("\n======== readlines 로 읽기 ========\n")

# f = open("./day1219/새파일.txt",'r',encoding="utf-8")
# lines = f.readlines() # 첫 번째 출을 반환
# print(lines)

# for line in lines:
#     line = line.strip()
#     print(line)

# f.close()



# print("\n======== read 로 읽기 ========\n")

# f = open("./day1219/새파일.txt",'r',encoding="utf-8")
# data = f.read() #파일 내용 전체를 문자열로 반환
# print(data)
# f.close()



# print("\n======== 객체로 읽기 ========\n")

# f = open("./day1219/새파일.txt",'r',encoding="utf-8")
# for line in f:
#     print(line)
# f.close()



# print("\n======== 추가하기 모드 ========\n")


# f = open("./day1219/새파일.txt",'a',encoding="utf-8")
# for i in range(11,21):
#     data = f'{i}번째 줄입니다\n'
#     f.write(data)

# f.close()


# print("\n======== with문과 함께 사용하기 ========\n")


# f = open("./day1219/새파일.txt",'w',encoding="utf-8")
# f.write("Life is too short, you need python")

# f.close()

# # 위 내용 이랑 똑같이 작용

# with open("./day1219/poo.txt",'w', encoding='utf-8') as f:
#     f.write("Life is too short, you need python")


print("\n======== os.path.exists ========\n")

import os

file_path = './poo.txt'

if not os.path.exists(file_path):
    with open(file_path,'w',encoding='utf-8') as f:
        f.write("Life is too short, you need python")
