from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 로드
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print(X.head())
print()
X.info()

print(y) # 양성 1, 악성 0

y = 1 - y

print(y) # 양성 0, 악성 1

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# stratify=y 클래스 비율 쏠리지 않도록

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
y_proba = lr.predict_proba(X_test)[:, 1]

print('\n======= 예측 클래스 ======\n')
print(y_pred)

print('\n======= 예측(악성일) 확률 ======\n')
print(y_proba.round(3))


# ========================================================

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report, RocCurveDisplay

# 지표 계산
acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

print('[Metrics]')
print(f'Accuracy : {acc:.4f}')
print(f'Precision : {pre:.4f}')
print(f'Recall : {rec:.4f}')
print(f'F1-score : {f1:.4f}')
print(f'Roc Auc : {auc:.4f}')
print()

print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))
print()

print('Classfication Report')
print(classification_report(y_test, y_pred, digits=4))

'''
양성 - 암 환자, 스팸메일

TP (진짜 양성): 암 환자를 스팸을 잘 찾아냄          / 스팸메일 잘 걸러냄
FN (가짜 음성): 암 환자인데 아니라고 분류 (놓침)    / 스팸인데 아니라고 분류
FP (가짜 양성): 암환자 아닌데 맞다고 분류 (오해)    / 스팸 아닌데 스팸으로 분류
TN (진짜 음성): 아닌사람 아닌걸로 잘 분류           / 스팸 아닌거 아닌걸로 잘 분류

Confusion Matrix
[[70  2]   TP  FN
[ 7 35]]   FP  TN

==========================================
재현율 (Recall)
Recall = TP / (TP + Fn)

실제 악성 중에서 모델이 놓치지 않고 잡아낸 비율
값이 높을 수록 암 환자를 놓치지 않는다는 의미
FN(놓친 악성)이 줄어들 수록 Recall 업

====================================
위양성률 (False, Positive Rage, FPR)
FPR = FP / (FP + TN)

스팸메일 아닌데 스팸메일로 분류한 비율
값이 높을 수록 (일반메일을) 스팸으로 판단하는 경우가 많다는 뜻
ROC 곡선의 X축이 FPR 이다.

=======================================
모델의 임계값(threshhold)을 조정하면 Recall 과 FPR이 trade-off 관계를 가진다
임계값을 낮추면: Recall ↑ (많이 잡음), but FPR ↑ (오진도 늘어남)
임계값을 높이면: Recall ↓ (많이 놓침), but FPR ↓ (오진 줄어듬)

=======================================
정밀도 (Precision)
Precision = TP / (TP + FP)

모델이 악성이라고 예측한 것 중에서 실제 악성 비율
FP를 줄이자 -> 판정의 신뢰도

'''

