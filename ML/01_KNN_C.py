
# 도미 데이터 35
 
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 
                32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 
                35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]


bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 
                500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 
                620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

import matplotlib.pyplot as plt

# plt.scatter(bream_length, bream_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


# 빙어 데이터 14

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = [[l,w] for l, w in zip(length, weight)]

print('\n============== 인풋 데이터 ==============\n')
print(fish_data)

print('\n============== 타겟 데이터 (정답지) ==============\n')

# 도미 1 빙어 0

fish_target = [1]*35 + [0]*14
print(fish_target)


# K-최근접 이웃 알고리즘
# KNN (K-Nearest Neighbors)
# K - 근처 몇 개의 이웃을 참고할지 (K개)


from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# KNN 분류 학습
kn.fit(fish_data, fish_target)
print('\n====== kn 모델 학습 완료 ======\n')


# 빙어와 도미 그래프

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.scatter(30, 600, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


print('\n======= 30/600 물고기 예측 =======\n')
print(kn.predict([[30, 600]]))

print('\n======= 학습 데이터로 score 계산1 =======\n')
print(kn.score(fish_data, fish_target))


# 학습데이터 준비 (인풋데이터, 타겟데이터)
# 모델 선정 및 불러오기
# 모델 학습
# 스코어 확인 / 특정 데이터 예측
# (그래프)

# KNN - 모든 점의 거리를 다 계산해서 가장 가까운 5개의 이웃을 보고 분류
# 모든 데이터의 정보를 가지고 있음

print('\n====== 저장된 정보 ======\n')
print(kn._fit_X)

print('\n====== 저장된 정답지 ======\n')
print(kn._y)


# 디폴트 이웃 수 = 5
# K를 49로 바꿔서 다시 학습

kn49 = KNeighborsClassifier(n_neighbors=49)

# 학습!
kn49.fit(fish_data, fish_target)

# 학습 데이터지만 예측 score 내보기
print('\n======= 학습 데이터로 score 계산2 =======\n')
print(kn49.score(fish_data, fish_target))


print('\n======= 랜덤 생선 3마리 예측 =======\n')
print(kn49.predict([[30, 600], [20, 100], [15, 70]]))

# 응용 예제

#for 문 돌려서, 이웃수 5부터 시작해서 50까지 돌리면서 과연 이웃수 몇일 때 스코어 1에서 떨어지나


for k in range(5, 51):
    kn = KNeighborsClassifier(n_neighbors=k)
    kn.fit(fish_data, fish_target)
    score = kn.score(fish_data, fish_target)
    