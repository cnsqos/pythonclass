import pandas as pd

fish = pd.read_csv('./data/fish_data.csv')

print(fish.head())
print()
fish.info()

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()
'''
['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
참붕어 붉은줄납줄개 백어 파르키 농어 가시고기 빙어
'''

# 인풋 데이터
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]

print(fish_input.head())
print()

# 타겟 데이터
fish_target = fish['Species']

# 훈련/테스트 셋 분리
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42
)

# 스케일링(표준화)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

#==================================
# 로지스틱 회귀로 다중분류 수행
# c = 계수제곱규제(L2), 작을 수록 규제 커짐. 기본값 1

import numpy as np
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)
print('\n ======== 로지스틱리그레션 학습 완료 ==========\n')

print('훈련 스코어:', lr.score(train_scaled, train_target))
print('테스트 스코어:', lr.score(test_scaled, test_target))

print('\n====== 상위 5개 행 예측 ======\n')

print(lr.predict(test_scaled[:5]))

print('\n====== 상위 5개 행 클래스별 확률 ======\n')

proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))

print('\n====== 클래스 종류 ======\n')
print('\n클래스 순서:', lr.classes_)
print()

# 파라미터 5 + 1 ==> 7세트
# 각 클래스별로 선형 방정식 존재
print('\n ===== 파라미터 개수 =======\n')
print(lr.coef_.shape, lr.intercept_.shape)

print('\n ===== 상위 5개행 클래스별 z값 출력 =======\n')
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))


from scipy.special import softmax

print('\n ====== 소프트맥스 함수에 z 값 대입 ========\n')

proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))

