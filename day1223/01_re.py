import re


p = re.compile('ab*')

# p = 패턴객체
# 패턴객체 메서드의 종류

# match() - 문자열이 처음부터 정규식과 매치되는지 조사
# search() - 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() - 정규식과 매치되는 모든 무자열을 리스트로 반환
# finditer() - 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환
# sub() - 정규식으로 매치되는 부분을 다른 문자열로 치환


p = re.compile('[a-z]+')
m = p.match("python")
print(m)