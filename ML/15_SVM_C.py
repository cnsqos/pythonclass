'''
# 고차원 데이터에 강하다
# 과적합을 피할 수 있다.
# 데이터를 가장 잘 나누는 결정경계를 찾는 분류 모델
# 효과적인 최적화
# 데이터가 적을때 상대적으로 성능이 좋음
# 커널트릭 - 비선형 분류
# 특성수가 많고 경계가 명확한 경우 쓰면 좋음
# 파라미터가 적어서 튜닝 지옥을 피할 수 있다.
# 마진을 최대화 하는 것이 목표
'''

# SVM (support vector machine) - 분류계의 전통 강자
# 분류 SVC, 회귀 SVR
# 결정경계를 찾는 모델
# 마진 - 서포트 벡터와 결정경계와의 거리
# 마진을 최대화 하는것을 목표로 함

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 데이터 준비(직접 만들기)
X, y = make_classification(n_samples=400, n_classes=2, n_features=2, n_redundant=0, random_state=42)

# n_samples 총 샘플 수
# n_classes 클래스 수
# n_features 특성 수
# n_redundant 불필요한 특성 수 (특성간의 선형 조합으로 만들 수 있는 특성)

print(X)
print(y)