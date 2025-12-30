import pandas as pd

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']


print('\n=========== 단위연산 ==============')

print(df.head(3))
print()

# mpg(mile per gallon) kpl(kilometer per liter)
# 1 마일 = 1.61km     1갤런 = 3.785412리터

mpg_to_kpl = 1.61 / 3.79


# kpl 열 추가
df['kpl'] = df['mpg'] * mpg_to_kpl

print(df.head(3))
print()

df['kpl'] = df['mpg'].round(2)

print(df.head(3))
print()


print('\n=========== 자료형 변환1 ==============')

# 각 열의 자료형 확인
print(df.dtypes)
print()
df.info()
print()


# horsepower의 고윳값 확인
print(df['horsepower'].unique())
print()

# 누락데이터('?') 삭제
import numpy as np

df['horsepower'] = df['horsepower'].replace('?',np.nan)
df = df.dropna(subset=['horsepower'], axis=0)
df['horsepower'] = df['horsepower'].astype('float')

df.info()

# 필터링을 이용해서 ?가 아닌 행들만 필터링 -> 그다음 astype('float)

df = df[df['horsepower'] != '?']
df['horsepower'] = df['horsepower'].astype(float)

df.info
print()
print(df['horsepower'].dtypes)


print('\n=========== 자료형 변환2 ==============')

# origin 컬럼 고윳값 확인

print(df['origin'].unique())
print()

# 정수형 데이터 [1 3 2] 를 문자형으로 반환
# {1:'USA', 2:'EU', 3:'JPN'}

df['origin'] = df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'})

print(df['origin'].unique())
print()
df.info()
print()
print(df.dtypes)
print()
print('origin 칼럼 데이터 타입 :', df['origin'].dtypes)
print()
print(df)
# origin 칼럼 데이터 타입: object


print('\n=========== 자료형 변환3 ==============')

# object -- 행마다 문자열 전체를 저장 -- 메모리 낭비
# category -- 내부적으로 정수 코드로 저장, 실제 값은 별도 보관
# 연산속도 향상 / 순서가 있는 범주 표현 가능


df['origin'] = df['origin'].astype('category')
print(df.dtypes)

print('\n=========== 순서가 있는 범주 =============\n')

df_grade = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'grade' : ['A', 'C', 'B', 'D', 'F']
})

print(df_grade)
print()
df_grade.info()
print()

df_grade['grade'] = pd.Categorical(
    df_grade['grade'],
    categories=['F', 'D', 'C', 'B', 'A'],
    ordered=True
)

df_grade.info()
print()

df_grade = df_grade[df_grade['grade'] >= 'C']
print(df_grade)


print('\n======================\n')

# model year 컬럼 샘플 3개만 뽑아보세요
# model year 데이터 타입을 category로 변환 후 컬럼샘플 3개 뽑기

print(df['model year'].sample(3))
print()

df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
print()


