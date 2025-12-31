import pandas as pd
import numpy as np

print('\n============== 문자열 인덱스 ==============')

dates_str = ['2025-01-01', '2025-01-02', '2025-01-03', '2025-02-01', '2025-02-02']
sales = [200, 250, 300, 150, 400]
df_str = pd.DataFrame({'sales': sales}, index=dates_str)

print(df_str)

# 문자열 인덱스로 특정 월 데이터 선택 (2월 데이터)


feb_sales_str = df_str[[i.startswith('2025-02') for i in df_str.index]]
print(feb_sales_str)

# df_str.loc['2025-02'] ???

print('\n============= DatetimeIndex ==============')
dates_dt = pd.to_datetime(dates_str)
df_dt = pd.DataFrame({'sales' : sales}, index=dates_dt)

print(df_dt)

feb_sales_dt = df_dt.loc['2025-02']
print(feb_sales_dt)


print('\n============= PeriodIndex ==============')

dates_pr = dates_dt.to_period('M')
df_pr = pd.DataFrame({'sales': sales}, index=dates_pr)

print(df_pr)

feb_sales_pr = df_pr.loc['2025-02']
print(feb_sales_pr)


print('\n====================================')

# 예제 데이터 생성 (2025년 1월 1일부터 2025년 3월 31일까지)
dates = pd.date_range('2025-01-01', '2025-03-31', freq='D')
sales = np.random.randint(100, 500, size=len(dates))

# DatetimeIndex 사용해서 데이터프레임 생성
df_datetime = pd.DataFrame({'sales': sales}, index=dates)

print(df_datetime)
print()
df_datetime.info()
print()

print('\n================= datetime 월별 합계 계산 ===================')

monthly_sum_dt = df_datetime.resample('M').sum()
print(monthly_sum_dt)

# PeriodIndex 사용해서 데이터프레임 생성

df_period = pd.DataFrame({'sales': sales}, index=dates.to_period('M'))

print('\n======== period 월별 합계 계산 =========')

monthly_sum_pr = df_period.groupby(df_period.index).sum()
print(monthly_sum_pr)