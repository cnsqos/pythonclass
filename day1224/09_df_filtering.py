# pip install seaborn

import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 데이터 불러오기
titanic = sns.load_dataset('titanic')

# loc 사용: 0~9행, age / fare
df = titanic.loc[0:9, ['age', 'fare']]
print(df)


print("\n========== 데이터 필터링 ===========\n")

print(df['age'])
print()
print(df['age'] < 20)
print()
print(df[df['age'] < 20])
print()


print("\n========== 논리연산자 ===========\n")

# 20살 이상
print(df.loc[~(df['age'] < 20)])
print()

# 10살 이상 & 20살 미만
mask1 = (titanic['age'] >= 10) & (titanic['age'] < 20)
print(titanic.loc[mask1].head())
print()


# 10살 이상인 여성
mask2 = (titanic['age'] >= 10) & (titanic['sex'] == 'female')
df_female_over10 = titanic.loc[mask2]
print(df_female_over10.head())


print("\n========== 행 컨디션 열 셀렉션 ===========\n")

# 조건 + 컬럼 선택 (age, sex)
df_female_over10 = titanic.loc[mask2, ['age', 'sex']]
print(df_female_over10.head())
print()




# or는 |기호 사용
# 10살 미만이거나 60살 초과인 사람만 필터링
# age who 컬럼만
# 10부터 19번까지 iloc로 뽑아보기


mask3 = (titanic['age'] < 10) | (titanic['age'] > 60)
df_young_old = titanic.loc[mask3, ['age', 'who']]
print(df_young_old.iloc[10:20])

print(mask3)
print()


titanic['df_y_o'] = mask3
print(titanic.head())
# print(titanic.head(100))

print("\n===============================\n")

# 탑승도시가 Queenstown, Southampton 인 두 곳만 필터링해서 head 프린트
mask1 = titanic['embark_town'] == "Southampton"
mask2 = titanic['embark_town'] == "Queenstown"
df_boolean = titanic[mask1 | mask2]
print(df_boolean.head())
print()


