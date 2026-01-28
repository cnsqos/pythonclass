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
    fig, axs= plt.subplots(rows, cols,
                          figsize=(cols*ratio, rows*ratio), squeeze=False)
    
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()


# 라벨이 0인 군집 - (112, 100, 100)
print(fruits[km.labels_==0].shape)

# 라벨별로 출력해보기
# draw_fruits(fruits[km.labels_==0])

# draw_fruits(fruits[km.labels_==1])

# draw_fruits(fruits[km.labels_==2])

# 분류해 놓은 세 군집 사진들의 픽셀별 평균
draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio=3)

# 인덱스 100번 사진의 클러스터별 중심거리
print(km.transform(fruits_2d[100:101]))

# 인덱스 100번 사진이 무슨 클러스터인지 확인
print(km.predict(fruits_2d[100:101]))

# 실제로 무슨 과일인지 확인
draw_fruits(fruits[100:101])

# 알고리즘 반복 횟수 (중심점이 몇 번 옮겨갔을까?)
print(km.n_iter_) # 4번

'''
실제에서는 클러스터가 몇개인지 알 수 없다.
클러스터를 늘려가면서 '이너셔' 변화를 확인해 봐야 한다.
이너셔 = 데이터별로 "클러스터 중심과의 거리 제곱합"
이너셔 작아지는 속도가 줄어드는 지점이 적정 클러스터이다. (엘보우 방법)
'''

# 최적의 K 찾기
inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)

plt.plot(range(2,7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

