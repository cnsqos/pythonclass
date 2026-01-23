'''
# 고차원 데이터에 강하다
# 과적합을 피할 수 있다.
# 데이터를 가장 잘 나누는 결정경계를 찾는 분류 모델
# 효과적인 최적화
# 데이터가 적을때 상대적으로 성능이 좋음
# 커널트릭으로 비선형 분류도 가능
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

# 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, stratify=y
)

# 스케일링
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# 모델 준비 (선형 커널)
lin_clf = SVC(kernel='linear', C=1.0, random_state= 42) # C 높을 수록 예민 (과대적합 될 수 있다.)

# 모델 학습
lin_clf.fit(X_train, y_train)

# 테스트 데이터 예측
y_pred_lin = lin_clf.predict(X_test_sc)


# 모델 성능 평가

print('LinearSVC 정확도:', accuracy_score(y_test, y_pred_lin))
print()
print(classification_report(y_test, y_pred_lin))
print()
print('혼동행렬:\n', confusion_matrix(y_test, y_pred_lin))
print()

# =====================================

# RBF 커널 (비선형 경계학습)
# Radial Basis Function (방사 기저 함수)

rbf_clf = SVC(kernel='rbf', C=1000, gamma=10, random_state=42)
# gamma 값이 높을 수록 (과적합 위험)

'''
C - 모델이 오류를 얼마나 용인할지 결정 (클수록 용인 안함)
gamma - 한 점이 다른 점에 영향을 미치는 거리 (클수록 영향 범위 작음 -> 민감)
'''

rbf_clf.fit(X_train, y_train)
y_pred_rbf = rbf_clf.predict(X_test_sc)
print()
# 모델 성능 평가

print('[RBF SVC] LinearSVC 정확도:', accuracy_score(y_test, y_pred_rbf))
print()
print(classification_report(y_test, y_pred_rbf))
print()
print('[RBF SVC] 혼동행렬:\n', confusion_matrix(y_test, y_pred_rbf))
print()


# ======================================================

# 결정징계 시각화
def plot_decision_boundary(model, X_sc, y, title):
    # 그리드 생성
    x_min, x_max = X_sc[:,0].min()-1, X_sc[:,0].max()+1
    y_min, y_max = X_sc[:,1].min()-1, X_sc[:,1].max()+1
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300)
    )

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# 등고선과 산점도
    plt.figure(figsize=(5, 4))
    plt.contourf(xx, yy, Z, alpha=0.25)
    plt.scatter(X_sc[:,0], X_sc[:, 1], c=y, edgecolors='k', s=30)
    plt.title(title)
    plt.xlabel('x1 (scaled)')
    plt.ylabel('x2 (scaled)')
    plt.tight_layout()
    plt.show()

# ======================================================

# plot_decision_boundary(lin_clf, X_train_sc, y_train, 'LinearSVC (trian)')
# plot_decision_boundary(rbf_clf, X_train_sc, y_train, 'RBF SVC (trian)')
print()

# =========================================

x = np.linspace(-2, 2, 5)
x = np.linspace(-2, 2, 5)
print(x)
print(y)
print('\n==============================\n')

xx, yy = np.meshgrid(x, y)

print(xx)
print('\n==============================\n')
print(yy)
print('\n==============================\n')
print(xx.ravel())
print('\n==============================\n')
print(yy.ravel())
print('\n==============================\n')
print(np.c_[xx.ravel(), yy.ravel()])
print('\n==============================\n')
print(rbf_clf.predict(np.c_[xx.ravel(), yy.ravel()]))
print('\n==============================\n')
print(rbf_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape))
Z = rbf_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
print('\n==============================\n')
plt.contourf(xx, yy, Z)
plt.show()




