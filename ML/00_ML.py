''' ======= 머신러닝 =======
- 데이터 준비 - train_input, train_target / test_input, test_target

- 모델 준비 - 모델 옵션 설정
- 모델 학습 - 모델.fit(인풋, 타겟)
- 모델 평가 - score, accuracy_score 등
- (그래프)
- (예측)

fit, transfrom, score, predict, reshape
'''


''' ======= models =======
<KNN> K-최근접 이웃 모델
KNeighborsClassifier (분류) - 가장 가까운 이웃들을 조사하여 클래스 판단 (빙어vs도미)
KNeighborsRegressor (예측) - 가장 가까운 이웃들의 평균으로 예측 (길이로 무게 예측)

<LinearRegression> 선형회귀
- LinearRegression (예측) - (y = ax + b)
    데이터를 가장 잘 대표하는 회귀선을 찾는다.
    즉, a b (파라미터)를 찾는 것 (a = 웨이트(가중치), b = 바이어스(편향))
    x = 특성 값, y = 예측 값
    손실함수 MSE 를 최소화 하는 a b를 찾는 것. (MSE를 미분하여 찾음) ==> 더 공부.


<Ridge, Lassso> 릿지, 라쏘 회귀
- Ridge (예측/회귀) - 파라미터들을 규제하여 안정적인 모델 학습 가능.
    선형회귀 손실함수(MSE)에 정규항 L2를 추가.
    파라미터를 조정하지만 0으로 만들진 않음.

- Lasso (예측) - 파라미터들을 규제하여 안정적인 모델 학습 가능.
    선형회귀 손실함수(MSE)에 정규항 L1를 추가.
    필요 없는 특성의 파라미터는 0으로 만들어 버림.

<LogisticRegression> 로지스틱 리그레션
    - 선형회귀의 선형방정식 결과 = z( z = a1X1 + a2X2 ... + anxn + b)
        선형회귀의 선형방정식 결과를 시그모이드 함수에 통과시켜서 0 or 1 로 분류 문제 수행.
        다중분류도 가능함 (ovr) - 이진분류를 여러개 수행
        다중분류(softmax) - z를 소프트맥스 함수에 통과시켜서 다중분류 수행

<SGD> 확률적 경사하강
    선형 방정식을 기반으로 회귀/예측 수행
    경사하강을 기반으로 하는 일반적인 모델
    데이터를 1개씩 넣어가면 파라미터 업데이트
    추가 학습이 가능한 모델
    - SGDClassifier - 분류
    - SGDRegressor - 예측

    
<SVM> 서포트 벡터 머신
    svc (분류) - 클래스 간의 마진을 최대화하는 선을 찾는다.
                중/소 규모 데이터, 고차원 데이터에 강함.
                커널트릭으로 비선형 데이터 분류 가능
                비교적 경계가 확실한 데이터에 쓰면 좋음
    
    svr (회귀) - 예측 함수 구간에 엡실론 만큼의 허용 오차 구간 생성
                엡실론 튜브 안의 오차는 손실로 보지 않는다
                허용 오차 구간 밖에 있는 점들이 서포트벡터
                엡실론 : SVR 에서 허용 오차 폭


<Tree 계열>
    DecisionTree - 노드를 분할하며 데이터 분류, 지니불순도가 가장 작아지는 임계값(분할 조건) 선택
            - DecisionTree Classifier - 분류된 노드의 샘플들의 클래스 다수결로 결정
            - DecisionTree Regressor - 분류된 노드의 샘플들의 평균으로 결정 (MSE 낮을때)

    RandomForest - 결정나무 100개의 숲, 부트스트랩 샘플링, 랜덤 특성 선택, oob_score
                 - 단일 결정 나무보다 랜덤성을 추가하여 일반화 성능 높임

    ExtraTrees - 결정나무 100개의 숲, 랜덤 특성 선택, 랜덤 임계값 생성
               - 랜덤 포레스트보다 랜덤성 더 추가 (속도, 일반화 성능 up)

<GBM 계열> - 그라디언트 부스팅
    평균으로 시작하여 잔차들을 학습하는 얕은 트리를 추가하는 '잔차학습' 방법               
    GradientBoosting
    HistGradientBoosting - 데이터를 128/255 등 구간에 나누어 그 경계값만 분할 임계점 후보로 항여, 속도를 높임.

    <XGBoost>
        클래식 GradientBoosting의 성능을 한층 높인 모델.
        빠른 학습, 결측/희소 데이터 처리, 병렬화/ 메모리 효율, 규제 옵션 등등.

    <LightGBM>
    

'''



'''
============================ ETC =======================

<데이터 분할> train_test_split
데이터 준비 과정에서 데이터를 훈련세트와 테스트세트로 나누는 것.

<스케일링>
    필요한 경우 데이터를 스케일링 해 주어야 한다.
    - StandardScaler - 평균 0, 표준편차 1로 변환
    - MinMaxScaler - 최솟값 0, 최대값 1 범위로 변환
    - RobustScaler - 중앙값과 IQR 사용해서 스케일링
    - 

<특성공학>
    - PolynomialFeatures - 특성을 인위적으로 늘리는 작업
    - 그 외 (추후 추가)

<옵션탐색>
    각 모델마다 최적의 옵션을 탐색하여 최고 모델의 최고 성능을 찾아내는 활동

<score>
- 분류 - 맞춘개수 / 테스트개수
- 회귀(예측) - R^2 (결정계수)

<metrics> 여러가지 성능 평가지표
- 분류 - accuracy_score (정확도), precision_score (정밀도), recall_score (재현율), f1_score (조화평균), roc_auc_score(auc 면적)
                                             
        confusion_matrix, classification_report
            
        재현율 vs 위양성률


- 회귀 - mean_absolute_error (MAE) 평균 절대 오차
        mean_squared_error (MSE) 평균 제곱 오차
        np.sqrt(mean_squared_error) (RMSE) 루트 평균 제곱 오차
        r2_score(결정계수)
        score (결정계수)

'''