'''
EPS(Earnings Per Share, 주당순이익)
한 주당 회사가 얼마나 벌었는지

BPS (Book-value Per Share, 주당순자산)
한 주당 회사가 가진 순자산

PER (Price Earnings Ratio, 주가수익비율)
이익 대비 주가가 비싼지 싼지

PBR (Price Book-value Ratio, 주가순자산비율)
자산 대비 주가수준
'''

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

# 주가 데이터 (stock price)
df1 = pd.read_excel('data/stock_price.xlsx')
print(df1)
print()

# 주식 가치평가 데이터 (stock_valuation)
df2 = pd.read_excel('data/stock_valuation.xlsx')
print(df2)
print()

# 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1, df2, how='inner', on='id')
print(merge_inner)
print()


print('\n======= 데이터프레임 합치기 - 교집합 ========\n')


merge_inner2 = pd.merge(df1, df2, how='inner', left_on=['id', 'stock_name'], right_on=['id','name'])
'''
id <-> id
stock_name < - > name
두가지 항목이 모두 같아야 하는 이너머지.
ex) '종근딩' 으로 바꾸면 종근당 != 종근딩 이어서 해당 항목은 빠짐

'''
print(merge_inner2)
print()


print('\n======= 데이터프레임 합치기 - 합집합 ========\n')

# 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1, df2, how = 'outer', on='id')
print(merge_outer)
print()

# 왼쪽 기준으로 합치기
merge_left = pd.merge(df1, df2, how = 'left', on = 'id')
print(merge_left)
print()

# 오른쪽 기준으로 합치기
merge_right = pd.merge(df1, df2, how = 'right', on = 'id')
print(merge_right)
print()

# 교차 조인
merge_cross = pd.merge(df1, df2, how='cross')
print(merge_cross)
print()

# df1 에서 price가 5000 미만인 행들만 필터링
price = df1[df1['price'] < 5000]
print(price)
print()

value = pd.merge(price, df2, on = 'id')
print(value)
print()

# 두개를 이너 머지 한 상태에서 price < 50000 으로 필터링 한 것과 같다.
value2 = pd.merge(df1, df2)[pd.merge(df1, df2)['price'] < 5000]
print(value2)
print()

  
print('\n=============================\n')

# 데이터프레임 생성
sdf1 = pd.DataFrame({'employee': ['Alice', 'Sam', 'Eva'],'department':['HR', 'Tech', 'HR']})

sdf2 = pd.DataFrame({'employee': ['Eva', 'Alice', 'Sam'], 'start_year': [2018, 2019, 2020]})

print(sdf1)
print(sdf2)

# 중복이 있냐 ㅇ벗냐

# one-to-one 조인
result_one_to_one = pd.merge(sdf1, sdf2, on='employee')
