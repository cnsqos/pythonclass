import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width', True)

fruit_names = pd.Series(["Apple", "Banana", "Cherry"])

print(fruit_names)
print()


fruit_name2 = pd.Series(["Apple", "Banana", "Cherry"], dtype="string")
print(fruit_name2)
print()


fruit_name3 = pd.Series(["Apple", "Banana", "Cherry"], dtype=pd.StringDtype())
print(fruit_name3)
print()


fruit_name4 = fruit_names.astype('string')
print(fruit_name4)
print()


print('\n=========== 문자열 메서드 =============\n')


ser = pd.Series(["Apple_사과-", "Banana_바나나", "Cherry_체리", np.nan],
                index=["First ", " Second", " Third", "Fourth"])

print(ser)
print()


ser2 = ser.astype('string')
print(ser2)
print()

print(ser.str.upper())
print()
print(ser.str.len())
print()
print(ser.str.split("_"))
print()
print(ser.str.split("_", expand=True))
print()
print(type(ser.str.split("_", expand=True)))
print()
print(ser.str.split("_").str.get(0))
print()
print(ser.str.split("_").str.get(1))
print()


idx = ser.index
print(idx)
print(idx.str.strip())
print(idx.str.lstrip())
print(idx.str.rstrip())
print()

# 원본 인덱스 스트립 정리하기

idx = ser.index.str.strip()
print(ser)
print()


print('\n=========== replace에서 정규식 사용/미사용 =============\n')

# _ 를 : 로 바꿀것입니다.
print(ser.str.replace("_", ":", regex=False))
print()

print(ser.str.replace("[^a-zA-Z\s]", "", regex=True))
print()


print('\n=========== 문자열 인덱싱 =============\n')

print(ser)
print(ser.str[0])
print()

print(ser.str[0:4])
print()


print('\n=========== contains 와 fullmatch =============\n')

contains_A = ser.str.contains("A", na=False)
print(contains_A)
print()

contains_pattern = ser.str.contains(r"[AB][a-z]+")
print(contains_pattern)
print()


fullmatch_pattern = ser.str.fullmatch(r"[AB][a-z가-힣_]+")
print(fullmatch_pattern)
print()



