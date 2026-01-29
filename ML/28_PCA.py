# PCA (Principal Component Analysis)    - 주성분 분석
# 데이터 압축, 차원 축소, 정보 손실 최소화
# 단점 - 직관적 설명이 어려움


import numpy as np

# 과일사진 데이터 로드
fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

# 주성분 분석
# 2차원 배열 입력을 기대
# 사진인지 아닌지 상관 없음

from sklearn.decomposition import PCA

pca = PCA(n_components=50) # 주성분을 50개로!
pca.fit(fruits_2d) # 주성분 분석 완료

# 주성분 모양 (50, 10000)
print('\n======= 주성분 모양 =======\n')
print(pca.components_.shape)

import matplotlib.pyplot as plt

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


print('\n======= 주성분 출력 =======\n')
print(pca.components_)

# 주성분 그려보기
draw_fruits(pca.components_.reshape(-1, 100, 100))

print('\n======= 원본 배열 크기 =======\n')
print(fruits_2d.shape) # 300, 10000 - 10000차원 짜리 점 300개

# 주성분으로 차원 축소
fruits_pca = pca.transform(fruits_2d)

print('\n======= 차원 축소 후 크기 =======\n')
print(fruits_pca.shape) # 300, 50 - 50 차원 공간에 점 300개

print('\n======= 첫 번째 점 출력 (50차원) =======\n')
print(fruits_pca[0]) # 더이상 픽셀은 아니다. # 첫 번째 과일 사진의 정보를 축소해서 담고 있을 뿐


# 다시 복원해서 그려보기 - 최대한 비슷하게 복원해서 그려줌.
fruits_inverse = pca.inverse_transform(fruits_pca)

print('\n======== 복원 후 크기 ========\n')
print(fruits_inverse.shape) # 300, 10000

fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)

# 100장씩 그리기
for start in [0, 100, 200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print()


# 설명된 분산 - 50개의 주성분이 원본을 얼마나 잘 표현 했을까?
print('\n======= 주 성분별 설명 퍼센티지 ======\n')
print(pca.explained_variance_ratio_)

