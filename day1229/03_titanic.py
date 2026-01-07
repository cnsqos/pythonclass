# 타이타닉 로드하기 (시본)
# 데이터 구조 확인
# 80세 노인분의 생존 여부
# 승객의 평균나이, 평균요금
# age의 결측치를 age의 평균으로 채우기
# deck 컬럼 제거
# age, parch, class 열만 선택하여 보기
# age, parch, class 열만 선택하여 랜덤 추출
# FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신)
# (로 해서 총 가족 인원수 컬럼 만들어보기)
# IsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 )
# 불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링
# 남성과 여성의 평균 나이 비교
# id 라는 이름으로 정수 인덱스 주기


import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 데이터 불러오기
titanic = sns.load_dataset('titanic')

# 데이터 구조 확인
print(titanic.info())
print(titanic.head())
print()

# 80세 노인의 생존 여부 확인
elderly = titanic[titanic['age'] >= 80]
print(elderly[['age', 'alive']])
print()

# 승객의 평균 나이, 평균 요금
print("평균 나이:", titanic['age'].mean())
print("평균 요금:", titanic['fare'].mean())
print()

# age의 결측치를 age 평균으로 채우기
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())
print()

# deck 컬럼 제거
titanic = titanic.drop(columns=['deck'])
print()

# age, parch, class 열만 선택하여 보기
print(titanic[['age', 'parch', 'class']].head())
print()

# age, parch, class 열만 랜덤 추출
print(titanic[['age', 'parch', 'class']])
print()

# FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신)
# (로 해서 총 가족 인원수 컬럼 만들어보기)
titanic['FamilySize'] = titanic['sibsp'] + titanic['parch'] + 1
print(titanic[['sibsp', 'parch', 'FamilySize']].head())
print()


# IsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 )
# 불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링
titanic['IsChild'] = titanic['age'] < 13
print(titanic[['age', 'IsChild']].head())
print()


# 남성과 여성의 평균 나이 비교
# print(titanic.groupby('sex')['age'].mean())
# print()
malemean = titanic[titanic['sex'] == 'male']['age'].mean()
print("남성 평균 나이:", malemean)
femalemean = titanic[titanic['sex'] == 'female']['age'].mean()
print("여성 평균 나이:", femalemean)
print()



# id 라는 이름으로 정수 인덱스 주기
titanic['id'] = range(1, len(titanic) + 1)
print(titanic[['id', 'age', 'sex']].head())
print()