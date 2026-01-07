import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 300)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]

df2 = pd.pivot_table(df,                           # 피벗할 데이터프레임
                      index=['class', 'survived'],   # 행 위치에 들어갈 열
                      columns='sex',                # 열 위치에 들어갈 열
                      values='fare',            # 데이터로 사용할 열
                      aggfunc=['mean','sum'],       # 데이터 집계 함수
                      observed=True)

print(df2)
print()


print(df.head())
print()

# stack 적용
# 멀티 컬럼이면 한번 할 때마다 한개씩 내려옴
df_stacked = df2.stack()
print(df_stacked)
print()

df_unstacked = df_stacked.unstack()
print()


df_unstacked2 = df_unstacked.unstack(level=0)
print(df_unstacked2)
print()

df_stacked2 = df_unstacked2.stack(level=1, future_stack=True)
print(df_stacked2)
print()

