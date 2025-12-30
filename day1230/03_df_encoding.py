
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('data\\auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horsepower 에 '? 들어있는 행 드랍 하고, 자료형 float으로 변경

import numpy as np

df['horsepower'] = df['horsepower'].replace('?', np.nan)
df = df.dropna(subset=['horsepower'])
df['horsepower'] = df['horsepower'].astype(float)

df.info()
print()
print(df.head(50))

print('\n=========== 구간 나누기 ============')

# 각 구간에 속하는 데이터 개수(count), 경계값 리스트(gin_dividers)반환
# bins = 3 로 하면 세 구간으로 균등분할

count, bin_dividers = np.histogram(df['horsepower'], bins=[50, 100, 200, 300])

print(bin_dividers)
print()
print(count)
print()
print(df.describe())
print()

# 빠진 6개 찾기

df2 = df[(df['horsepower'] < 50) | (df['horsepower'] > 300)]
print(df2)
print()


print('\n=========== pd.cut ============')



# bin_dividers 세구간 (50,100),[100,200] , [200,300]
bin_names = ['저출력', '보통출력', '고출력']


# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels=bin_names,
                      include_lowest=True) # a,b
print(df.head(100))
df.info() #hp_bin >>> category
print()



print('\n=========== 더미변수 ============')

# hp_bin 컬럼의 범주형 데이터를 더미 변수로 변환
horsepower_duummies = pd.get_dummies(df['hp_bin'])
print(horsepower_duummies.head(15))
print(type(horsepower_duummies))
print()


# hp_bin 컬럼의 범주형 데이터를 더미 변수로 변환
horsepower_duummies = pd.get_dummies(df['hp_bin'], dtype=float, drop_first=True)
print(horsepower_duummies.head(15))
print()



print('\n=========== 레이블 인코더 ============')

print(df)

# pip install scikit-learn

# from sklearn import preprocessing

# label_enconder = preprocessing.LabelEncoder()

# onehot_labeled = label_enconder.fit_transform(df['hp_bin'])
# print(onehot_labeled)
# print(type(onehot_labeled))
# print()

# onehot_labeled = pd.Series(label_enconder.fit_transform(df['hp_bin']))
# print(onehot_labeled)
# print(type(onehot_labeled))
# print()



# df['hp_bin_lb'] = onehot_labeled
# df.info()
# print(df.head(30))



from sklearn.preprocessing import LabelEncoder

df['hp_bin_lb'] = LabelEncoder().fit_transform(df['hp_bin'])
df.info()
print(df.head(30))


print('\n======== 원핫 인코더 ========\n')

from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder(sparse_output=False) # True / False
# 희소행렬
onehot_fitted = onehot_encoder.fit_transform(df[['hp_bin']])

print(onehot_fitted)
print()
print(type(onehot_fitted))


encoded_df = pd.DataFrame(
    onehot_fitted,
    columns=onehot_encoder.get_feature_names_out(['hp_bin'])
)

print(encoded_df)

#============================

print()
print(df['hp_bin'])
print(type(df['hp_bin']))
print()
print(df[['hp_bin']])
print(type(df[['hp_bin']]))