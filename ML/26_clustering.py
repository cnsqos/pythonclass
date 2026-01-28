# 군집화 (clustering)

import numpy as np
import matplotlib.pyplot as plt

# 과일 사진 불러오기
fruits = np.load('./data/fruits_300.npy')

# ====== 데이터 탐색 ======
print('\n ======= 과일 전체 배열 =========\n')
print(fruits)

print('\n======= 데이터 전체 shape ========\n')
print(fruits.shape)
# (300, 100, 100) 100 x 100 짜리 300장

print('\n ======= 첫 사진의 첫 행 =======\n')
print(fruits[0, 0, :])

# 사진 출력 - 흑백사진이기 때문에 cmap ='gray' 지정 해줘야 한다.
# 0~255 사이 숫자로 이루어짐, 255 일수록 하얀색
# 원래 바탕은 하얗고 사과는 어두운 사진인데 (사과 부분이 숫자가 낮다는 뜻)
# (모델 학습 등) 컴퓨터는 높은 숫자에 주목하기 때문에
# 우리는 바탕보다 물체에 주목해야 하기 때문에 '흑백 반전'을 미리 준 데이터임.
# plt.imshow(fruits[0], cmap='gray')
# plt.show()

# 그런데 보기에 불편하므로 색상 반전 트릭을 주겠다.
# (숫자를 바꾸는건 아님)

# plt.imshow(fruits[0], cmap='gray_r')
# plt.show()

# # 파인애플과 바나나도 뽑아보기
# fig, axs = plt.subplots(1, 2)
# axs[0].imshow(fruits[100], cmap='gray_r')
# axs[1].imshow(fruits[200], cmap='gray_r')

# plt.show()

# 과일별로 나누면서 사진을 1차원으로 변형
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)

print('\n====== 사과 데이터 확인 =======\n')
print(apple.shape) # (100, 10000)

print('\n======= 사과 사진별로 평균 =======\n')
print(apple.mean(axis=1))
# 하얀부분 (사과부분)이 많을수록 평균이 높을 것.
# 바나나 보다는 평균들이 전체적으로 높을 것으로 예상.


# 과일별로 평균내서 그래프 그려보기
# plt.hist(apple.mean(axis=1), alpha=0.8, label='apple')
# plt.hist(pineapple.mean(axis=1), alpha=0.8, label='pineapple')
# plt.hist(banana.mean(axis=1), alpha=0.8, label='banana')
# plt.legend()
# plt.show()

# # 픽셀 위치별로 과일별로 평균내서 그래프 그려보기
# plt.hist(apple.mean(axis=0), alpha=0.8, label='apple')
# plt.hist(pineapple.mean(axis=0), alpha=0.8, label='pineapple')
# plt.hist(banana.mean(axis=0), alpha=0.8, label='banana')
# plt.legend()
# plt.show()


# # 픽셀 위치별로 평균내서 (bar) 그래프 그려보기
# fig, axs = plt.subplots(1, 3 , figsize=(20, 5))
# axs[0].bar(range(10000), apple.mean(axis=0))
# axs[1].bar(range(10000), pineapple.mean(axis=0))
# axs[2].bar(range(10000), banana.mean(axis=0))
# plt.show()


# 픽셀 위치의 평균값들로 한 장의 (과일별) 사진 만들기
apple_mean = apple.mean(axis=0).reshape(100, 100)
pineapple_mean = pineapple.mean(axis=0).reshape(100, 100)
banana_mean = banana.mean(axis=0).reshape(100, 100)

fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()

# 모든 사진을 '평균 사과 사진' 으로 빼기
# 사과사진이라면 각가의 차이가 작겠죠
abs_diff = np.abs(fruits - apple_mean)

# 각각 빼기를 한 사진에 있는 숫자 10000개의 평균내기
abs_mean = np.mean(abs_diff, axis=(1, 2))
print(abs_mean.shape)

# ================= 넘피 argsort, sort ==================

arr = np.array([20, 30, 10])

print(np.sort(arr)) # [10 20 30] 정렬된 값들 반환
print(np.argsort(arr)) # [2 0 1] 정렬된 값들의 (원래) 인덱스 반환

# =======================================================

# 오차가 작은 그림 Top 100 의 인덱스 뽑아서
# 그 인덱스를 이용, 원본사진 불러오기

apple_index = np.argsort(abs_mean)[:100]
apple_index = apple_index.reshape(10, 10)

fig, axs = plt.subplots(10, 10, figsize=(10, 10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[apple_index[i, j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

# ===============================================================

fruits = np.load('./data/fruits_300.npy')

# 과일 사진을 무작위로 섞음

np.random.seed(42)
indices = np.arange(fruits.shape[0])
np.random.shuffle(indices)
fruits_shuffled = fruits[indices]

# 일단 잘 섞였는지 100개 이미지 띄워보기
fig, axs = plt.subplots(10, 10, figsize=(10, 10))

for i in range(100):
    ax = axs[i // 10, i % 10]
    ax.imshow(fruits_shuffled[i], cmap='gray_r')
    ax.axis('off')
plt.show()


# 각 이미지의 평균값 계산
fruit_means = fruits_shuffled.mean(axis=(1, 2))


# 평균값이 가장 작은 100개 이미지 선택
small_mean_indices = np.argsort(fruit_means)[:100]
dark_fruits = fruits_shuffled[small_mean_indices]


# 평균이 가장 작은 100개 이미지 확인

fig, axs = plt.subplots(10, 10, figsize=(10, 10))

for i in range(100):
    ax = axs[i // 10, i % 10]
    ax.imshow(fruits_shuffled[small_mean_indices[i]], cmap='gray_r')
    ax.axis('off')
plt.show()

