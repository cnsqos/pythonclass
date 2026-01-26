import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# 데이터 불러오기

# 반중력 물질을 개발해서 - 비행 판도를 바꾸겠다.
# 식물 에너지 시스템 - 에너지 판도를 바꾸겠다.

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.head())
print()
X.info()
print()
print(y.head())

