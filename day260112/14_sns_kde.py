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

# 영역 색깔 채움 fill = True
sns.kdeplot(x='age', data=titanic, hue='survived', fill=True, ax=axes['top_center'])

# 그래프 쌓기 multiple='stack'
sns.kdeplot(x='age', data=titanic, hue='survived', multiple='stack', ax=axes['bottom_center'])

# 그래프 비율 위아래로 채움 multiple='fill'
# bw_adjust=2.0 경계선 완만함 조절
sns.kdeplot(x='age', data=titanic, hue='survived', multiple='fill', bw_adjust=2.0, ax=axes['right'])

fig.suptitle('Titanic - Age Distribution')

axes['top_left'].set_title('KDE')
axes['bottom_left'].set_title('KDE (hue)')
axes['top_center'].set_title('KDE (fill=True)')
axes['bottom_center'].set_title('KDE (multiple - stack)')
axes['right'].set_title('KDE (multiple - fill)')



# ==================================================================

fig, ax1 = plt.subplots(figsize=(15, 6), constrained_layout=True)

sns.histplot(data=titanic,x='age',bins=30,stat='count',color='skyblue',alpha=0.6,ax=ax1)

ax1.set_xlabel('Age')
ax1.set_ylabel('Count (Histogram)', c = 'blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.grid(False)

sns.kdeplot(data=titanic, x='age',color='red', linewidth=2, ax=ax2)

ax2.set_ylabel('Density (KDE)', c = 'red')
ax2.tick_params(axis='y', labelcolor='red')

ax1.set_title('Titanic Age Distribution: Histogram vs KDE (Dual Y-Axis)')
plt.show()

