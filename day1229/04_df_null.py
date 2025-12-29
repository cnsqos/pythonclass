import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = sns.load_dataset('titanic')

print(df.head(20))
print()

print('\n============ 누락 데이터 확인 ============\n')


# deck 열 NaN 개수 확인하기

print(df['deck'].value_counts(dropna=False))
print()

print(df.head().isnull())
print()

print('\n============ missingno ============\n')

#pip install missingno

import missingno as msno
import matplotlib.pyplot as plt

#매트릭스 그래프

# msno.matrix(df)
# plt.show()

# 막대그래프
# msno.bar(df)
# plt.show()

# 히트맵 (누락 데이터 변수간 상관관계)
# msno.heatmap(df)
# plt.show()

# 덴드로그램
# msno.dendrogram(df)
# plt.show()


print('\n============ 누락 데이터 표현 ============\n')

# 기존 방식 (np.nan) : 정수형 자료가 float으로 변환
ser1 = pd.Series([1, 2, None])
print(ser1)

# 정수형이 그대로 유지됨 (결측치 pd.NA로 표현)
ser2 = pd.Series([1, 2, None], dtype = 'Int64')
print(ser2)

