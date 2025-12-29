# pip install seaborn

import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('data\\auto-mpg.csv', header=None)

# 열 이름 저장
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 연비, 실린더, 배기량, 마력, 차무게, 가속도, 출시연도, 제조국코드, 차이름

print()
print(df.head(50))
print()
print(df.tail())
print()
print(df.shape)
print()
df.info()
print()
print(df.dtypes)
print()
print(df['mpg'].dtypes) # 마일 퍼 갤런
print()


print('\n======== 산술정보 ========\n')

print(df.describe())
print()
print(df.describe(include='all'))
print()
print(df.describe(include='number'))
print()
print(df.describe(include='object'))
print()
print(df.count()) # 유효한 데이터 개수를 시리즈로 반환
print()

unique_values = df['origin'].value_counts()
print(unique_values)
# 1 미국/ 2 유럽 / 일본
print()

unique_values_ratio = df['origin'].value_counts(normalize=True)
print(unique_values_ratio)
print()


unique_values_percentage = (df['origin'].value_counts(normalize=True) * 100).round(1).astype(str) + '  %'
print(unique_values_percentage)
print()
