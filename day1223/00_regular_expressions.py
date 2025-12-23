# 정규 표현식(regular expressions)

data = """
park 800905-1049118
kim 700905-1059119
"""

# park 8800905-*******
# park 7000905-*******

for line in data.split("\n"):
    print(line)


print('123'.isdigit()) #
print('a123'.isdigit()) #

words = ['apple', 'banana', 'mango']
print(" ".join(words))

print()

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


print("============ re ============")

data = """
park 800905-1049118
kim 700905-1059119
"""

import re

for line in data.split("\n"):
    line = line.strip()
    if not line:
        continue

    result = re.sub(r'(\w+\s\d{6})-\d{7}', r'\1-*******', line)
    print(result)


pat = re.compile(r"(\d{6})[-](\d{7})")
print(pat.sub(r"\g<1>-*******", data))

pat = re.compile(r"(\d{6})-\d{7}")
print(pat.sub(r"\1-*******", data))


# (기초) 메타 문자
# . ^ $ * + ? { } [ ] \ | ( )

# ------- [] 문자 클래스 -------
# 대괄호 안의 한 글자
# [abc] >>> a,b,c 중 정확히 한 개의 문자가 있으면 매치
# "a" -> 매치
# "before" -> b가 있어서 매치
# "dude" -> 매치되지 않음

# [a-c] => [abc]
# [0-5] => [012345]
# [A-Z]] => 알파벳 대문자
# [가-하] => 모든 한글

# [^0-9] => 숫자가 아닌 모든 문자 (알파벳, 특수문자, 공백 등)
# [^abc] => a, b, c가 아닌 모든 문자
# [^A-Z] => 대문자 알파벳이 아닌 모든 문자

# -------- * 문자 --------
# * 바로 앞에 있는 문자 0~무한대 반복
# ca*t ==> ct cat caat caaat....


# \d ==> [0-9] ==> 숫자
# \D ==> [^0-9] ==> 숫자가 아닌것
# \s ==> (화이트스페이스) 공백 [ \t\n\r\f\v]
# \S ==> (화이트스페이스) 공백이 아닌것
# \w ==>문자 숫자 _ ==> [a-zA-z0-9_] + 유니코드 문자
# \W ==> \w 의 반대! [^a-zA-Z0-9_]


# --------- \b -------
# 단어 구분자. 화이트스페이스, 문장 시작, 기호 등에 의해 구분
# "cat catalog scatter cat bcat hello"
# 진짜 cat만 찾고 싶다.
# cat ==> cat cat cat cat cat cat
# \bcat\b ==> cat cat cat
# \scat\s ==> ...???


# -------- {} 문자 ---------
# {m} 바로 앞에 있는 문자 m번 반복
# {m,n} 바로 앞에 있는 문자 m~n 회 반복
# {m, } 바로 앞에 있는 문자 m 이상 반복
# {, n} 바로 앞에 있는 문자 n 이하 반복

# {0, } === *
# {1, } === +

# ca{2}t ==> caat
# ca{2,5}t ==> caat caaat caaat caaaaat

# -------- ? 문자 ---------
# 0qjs ghrdms 1qjs (skdhrjsk dksskdhrjsk
# {0, 1}과 동일
#
# ab?c ==> abc ac


# -------- .(dot) 문자 ---------

#\n 을 제외한 모든 문자
# a.b ==> ex) a1b aob a@b 등등 ==> a모든문자b
# a\.b 혹은 a[.]b ==> 'a.b
