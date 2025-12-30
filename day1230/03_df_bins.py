
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('data\\auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horsepower 에 '? 들어있는 행 드랍 하고, 자료형 float으로 변경

import numpy as np

df['horsepower'] = df['horsepower'].replace('?', np.nan)
df = df.dropna(subset=['horsepower'])
df['horsepower'] = df['horsepower'].astype(float)

df.info()
print()
print(df.head(50))

print('\n=========== 구간 나누기 ============')

# 각 구간에 속하는 데이터 개수(count), 경계값 리스트(gin_dividers)반환
# bins = 3 로 하면 세 구간으로 균등분할

count, bin_dividers = np.histogram(df['horsepower'], bins=[50, 100, 200, 300])

print(bin_dividers)
print()
print(count)
print()
print(df.describe())
print()

# 빠진 6개 찾기

df2 = df[(df['horsepower'] < 50) | (df['horsepower'] > 300)]
print(df2)
print()


print('\n=========== pd.cut ============')



# bin_dividers 세구간 (50,100),[100,200] , [200,300]

bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['']


