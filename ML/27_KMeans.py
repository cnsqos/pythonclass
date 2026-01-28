# 클러스터링 모델 KMeans

import numpy as np

fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

print(fruits_2d.shape) # (300, 10000)

# Kmeans 훈련

from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=42)