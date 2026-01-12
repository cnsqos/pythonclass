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


df = pd.read_excel('data/시도별_전출입_인구수.xlsx')

print(df.head())

df = df.ffill()
print(df.head())


# 전출지 = 서울, 전입지 = 서울빼고(전국) ==> 서울을 나간 사람들

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별' : '전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')
print(df_seoul)
print()

sr_one = df_seoul.loc['경기도']
print(sr_one)
print()

#===================================

# sr_one.index = sr_one.index.astype(str)
# plt.plot(sr_one)
# plt.show()


# 기본 그래프
plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.title('서울 -> 경기인구이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()


#============================================

# 기본 그래프 2
plt.figure(figsize=(14,7))
plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.xticks(rotation=90)
plt.title('서울 -> 경기인구이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'])
plt.show()

#============================================

# 스타일/마커

plt.style.use('bmh')

plt.figure(figsize=(14,5))
plt.plot(sr_one.index, sr_one.values,
         marker='s',
         markerfacecolor='red',
         markeredgecolor='blue',
         markeredgewidth=2,
         markersize=10,
         linestyle='dotted',
         label = '서울 -> 경기'
         )
# plt.title('서울 -> 경기인구이동') 라벨

plt.xticks(rotation='vertical', size=10)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)
plt.legend(labels=['서울 -> 경기'])
plt.show()

