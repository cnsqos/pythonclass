# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
#한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# 음수표기
plt.rcParams['axes.unicode_minus'] = False

#터미널 너비
pd.set_option('display.width', 500)


#=====================================================


samsung_revenue = pd.read_csv('./data/삼성전자_분기별_매출액.csv')
samsung_revenue.sort_values(by='quarter', inplace=True)
print(samsung_revenue)
print()

# 그래프 1개 그려보기
# fig, ax = plt.subplots(figsize=(8,2))
# ax.plot(samsung_revenue['quarter'], samsung_revenue['value'])

# plt.annotate('테스트',
#              xy=(1,6.5e13), #'2023-Q3' 가능
#              )
# plt.show()

# 그래프 2개 그려보기
# fig, axes = plt.subplots(1,2, figsize=(12,5))
# axes[0].plot(samsung_revenue['quarter'],samsung_revenue['value'])
# samsung_revenue['value'].plot(ax=axes[1],marker='<')
# plt.show()

# fig, axes = plt.subplots(2,2, figsize=(12,5))
# axes[0,1].plot(samsung_revenue['quarter'],samsung_revenue['value'])
# plt.show()


# subplot_mosaic 방법

fig, axes = plt.subplot_mosaic([['top_left','right'], ['bottom_left','right'],['a','a']], figsize=(12, 4))

axes['right'].plot(samsung_revenue['quarter'], samsung_revenue['value'])
plt.show()


'''
import matplotlib.pyplot as plt

plt.plot() - 디폴트가 선그래프일뿐.

plt.plot(시리즈)    x축 - 인덱스  y축 - 밸류
plt.show()

plt.plot(x축자료, y축자료)
plt.show()

plt.plot(데이터프레임) x축 - 인덱스  y축 - 밸류
데이터.plot()  -- 판다스에서 제공하는 형태인데 (내부적으로는 matplotlib)

plt.figure(figsize=(10,8))
plt.plot(x축, y축, marker='o', color='magenta', label='충청도')
경기도데이터.plot(디자인을 합니다.)

plt.title('인구이동')
plt.xlabel('년도')
plt.ylabel('이동인구')
plt.legend() --- 범례
plt.show()

fig, axes = subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y, 디자인)
axes[0, 1]
axes[1, 0]
axes[1, 1]

axes[0,0].set_title('뭐시기')
.
.
.

plt.show()
'''
