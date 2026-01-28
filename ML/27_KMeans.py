# 클러스터링 모델 KMeans

import numpy as np

fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

print(fruits_2d.shape) # (300, 10000)

# Kmeans 훈련

from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)
# 마치 10000차원 속에 있는 점 300개를 군집화 한 것.

print('\n====== 라벨링 결과 확인 =======\n')
print(km.labels_) # 클래스 0, 1, 2

print('\n======= 라벨별 카운트 확인 =========\n')
print(np.unique(km.labels_, return_counts=True))
# (array([0, 1, 2], dtype=int32), array([112, 98, 90]))
# 100개 100개 100개 였으면 만점. (..이지만 안됐음)


# 사진 여러장 넣으면 그려주는 함수 정의
# 최대 10열로 맞춰서 그려주는 함수

import matplotlib.pyplot as plt

# 입력 arr 예시 (98, 100, 100) --- 100x100 짜리 사진 98장

def draw_fruits(arr, ratio=1):
    n = len(arr)
    # 10개로 나눠서 올림함으로써 몇줄인지 확보
    rows = int(np.ceil(n/10)) # ceil : 올림
    # 한 줄밖에 없으면 열 개수는 샘플개수만큼, 그렇지 않으면 10개씩
    cols = n if rows < 2 else 10
    fig, axs= plt.subplot(rows, cols,
                          figsize=(cols*ratio, rows*ratio), squeeze=False)
    
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()


    