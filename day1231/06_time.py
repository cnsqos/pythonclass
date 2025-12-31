import pandas as pd

df = pd.read_csv('data\\stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df = df.set_index('new_Date')
df = df.drop('Date', axis=1)

ts = df.head(10)
ts = ts.sort_index()

print(ts)

print('\n======= shift ==========')
print(ts.shift(1))
print()
print(ts.shift(-2))
print()

print(ts.asfreq('5D'))
print()

print(ts.asfreq('5D', method='bfill'))
print()


print('\n======= resample ==========')

print(ts.resample('3B'))
print()

print(ts.resample("3B").sum())
print(ts.resample("3B").mean())
print(ts.resample("3B").median())



print('\n======= rolling ==========')

print(ts.rolling(window=3).sum())
print()
print(ts.rolling(window='3D').sum())
print()

