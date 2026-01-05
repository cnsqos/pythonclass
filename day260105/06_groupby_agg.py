import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]

# class로 그룹바이

grouped = df.groupby('class', observed=True)
print(grouped)
print()

# 표준편차 집계

std_all = grouped.std(numeric_only=True)
print(std_all)
print()

# groupby(~~~~, as_index=False) 옵션 추가해보기
std_all_index = df.groupby('class', as_index=False, observed=True).std(numeric_only=True)
print(std_all_index)
print()


print('\n=========================\n')

print(type(std_all))
std_all.info()
print()

# 그룹화(grouped) -> 집계(std_all) -> 컬럼선택(std_all['fare'])
print(std_all['fare'])
print()

# 그룹화 -> 컬럼선택 -> 집계
std_fare = grouped['fare'].std(numeric_only=True)
print(std_fare)

