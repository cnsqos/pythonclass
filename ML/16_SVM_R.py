# 서포트 벡터머신 회귀
# 예측함수 주변에 엡실론 만큼의 허용오차구간 생성(엡실론 튜브 안의 오차는 손실로 보지 않는다.)
# 과적합 비교적 덜하다

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# 데이터 만들기 (비 선형 데이터: y = sin(x))
rng = np.random.RandomState(42)
X = np.sort(5 * rng.rand(80, 1), axis=0) # 0 ~ 5 사이 숫자 80개 만들고 정렬
y = np.sin(X).ravel() + 0.1 * rng.randn(80)

# rand(80, 1) ==> 이상 1미만 균등 분포 난수를 80행 x 1열 형태로 생성
# randn(80) ==> 평균 0, 분산 1인 정규분포 난수 80개

print(X)
print(y)

svr = SVR(kernel='rbf', C=1, epsilon=0.1)
svr.fit(X, y)

X_test = np.linspace(0, 5, 200).reshape(-1, 1)
y_pred = svr.predict(X_test)

plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X_test, y_pred, color='navy', lw=2, label='SVR')
plt.xlabel('x')
plt.ylabel('y')
plt.title('SVR with RBF')
plt.legend()
plt.show()

