# 커널 밀도 추정 그래프 (Kernel Density Estiamte Plot)

'''
y축 수치는 의미 x

해석예시)
10살 ~ 20살 간격에 해당하는 그래프 넓이가 0.5 라면, 타이타닉 데이터에서 무작위로 사람을 한명 뽑았을 때, 나이가 10살 ~ 20살 일 확률이 50% 이다.

그래프의 총 넓이는 = 1
'''

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig, axes = plt.subplot_mosaic([['top_left','top_center', 'right'], ['bottom_left','bottom_center','right']], figsize=(15,6),
                         constrained_layout=True) # 간격 최대한 조정 옵션

sns.kdeplot(x='age', data=titanic, ax=axes['top_left'])

sns.kdeplot(x='age', data=titanic, hue='survived', ax=axes['bottom_left'])

sns.kdeplot(x='age', data=titanic, hue='survived', fill=True, ax=axes['bottom_center'])

plt.show()

