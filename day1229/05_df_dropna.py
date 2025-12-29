import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = sns.load_dataset('titanic')

print(df.isnull().sum(axis=0))
print()
print(df.notnull().sum(axis=0))

print('\n======== 누락데이터 제거 =========\n')

df_dropna1 = df.dropna()
df_dropna1.info()
print()

# 널값이 하나라도 있는 행은 제거

df_dropna1 = df.dropna() #axis=0 디폴트
df_dropna1.info()
print()

# 널값이 하나라도 있는 컬럼(열)은 제거
df_dropna2 = df.dropna(axis=1)
df_dropna2.info()
print()

# 유효한 데이터 500개 이상은 보존
df_dropna3 = df.dropna(axis=1, thresh=500)
df_dropna3.info()
print()

df_age = df.dropna(subset=['age'], axis=0)
df_age.info()
print()

# age, deck 중에 하나라도 널 값이 있으면 드랍
df_age_deck = df.dropna(subset=['age','deck'], axis=0) # how = 'any'
df_age_deck.info()
print()

# age, deck 모두 널이면 드랍
df_age_deck = df.dropna(subset=['age','deck'], how='all', axis=0) # how = 'any'
df_age_deck.info()
print()


print('\n======== age 널 값을 age 평균값으로 채우기 =========\n')

mean_age = df['age'].mean()
print(mean_age)
print()
df['age'] = df['age'].fillna(mean_age)
df.info()


print('\n======== embark_town (최빈값으로 대체) =========\n')

# 숫자형 산술정보
print(df.describe())
print()

# 문자형 통계정보
print(df.describe(include = object))
print()

# embark_town의 고윳값별 카운트
em_freq = df['embark_town'].value_counts(dropna=True)
print(em_freq)
print()


most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print('최빈값은:', most_freq)
print()
