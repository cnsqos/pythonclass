import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

# 1) 데이터 준비

wine = pd.read_csv('./data/wine_data.csv')
X = wine[['alcohol', 'sugar', 'pH']]
y = wine['class'] # 0 레드와인 / 1 화이트와인

# train/test 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# early stopping을 위한 valid 셋 분리
X_tr, X_val, y_tr, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42, stratify=y_train
)


# 2) 모델 & 옵션 설정
# pip install xgboost
from xgboost import XGBClassifier

xgb = XGBClassifier(
    # 기본성능/과적합 밸런스 관련
    n_estimators=2000,
    learning_rate=0.05,
    max_depth=4,            # 나무 최대 깊이
    min_child_weight=1,     # 분할 후 노드에 '최소한 이정도 정보량은 있어야 한다'
    gamma=0.0,              # 분할 최소 이득 (규제)
    subsample=0.8,          # row 샘플링 (트리 하나 만들 때마다 매번 다른 80% 샘플을 뽑아 사용)
    colsample_bytree=0.8,   # feature 샘플링 (트리 하나를 만들 때, 전체 특성 중 80%만 사용)
)

# 3) 학습



# 4) 평가


# 확률 / 예측


# 특성 중요도 확인


# 5) ROC Curve 그리기

