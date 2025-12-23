import re

print('\n========= 영어 단어만 추출 ===========')

text = "Python 정규식, Hello world! 123"
pattern = "[a-zA-Z]+" # 스펠링 여러개

pat = re.compile(pattern)
print(pat.findall(text))

# 축약형

print(re.findall(pattern, text))


print('\n========= 숫자만 추출 ===========\n')

# [2025, 12, 23, 4]

text = '오늘은 2025년 12월 23일, 수업은 4시간!'

pattern = r"\d+" # 붙어있는 숫자 여러개

print(re.findall(pattern, text))


print('\n========= 특정 단어로 시작하는 단어 찾기 =========\n')

text = "cat scatter cater catalog dog"
# cat 으로 시작하는 단어 찾기.
pattern = r"\bcat\w*"

mathces = re.findall(pattern, text)
print("cat으로 시작하는 단어: ", mathces)

# ['cat', 'cater', 'catalog']


print('\n========= or | ========\n')

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

print('\n========= 사용, 문자열 바꾸기 ========\n')

p = re.compile(r'blue|red')
m = p.sub('color', 'blue socks and red shoes')
print(m)

# color socks and color shoes


print('\n========= 모든 공백을 하나로 줄이기 ========\n')

text = '안녕하세요  반갑습니다 \t 저는 파이썬을   공부해요'
pattern = r'\s+'

result = re.sub(pattern, ' ', text )

print("공백 정리:", result)

# 공백 정리: 안녕하세요 반갑습니다 저는 파이썬을 공부해요 



print("\n======== 간단한 URL 찾기 ========\n")

text = "사이트 : http://example.com, 보안 : https://secure.org/path"
pattern = r"https?://[A-Za-z0-9./-]+"

urls = re.findall(pattern, text)

print("URL 추출:", urls)



print("\n======== 이메일 추출 ========\n")


text = """
문의: cs@test.co / backup: me.example+dev@sub-domain.example.com
스팸: a@b, user@.com, @nohost, 정상: hello.world@domain.io
"""

# 영문 점 기호 숫자 등

pattern = r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(pattern, text)

print("이메일 추출:", emails)
