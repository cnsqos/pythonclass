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

df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], :]
print(df_4)
df_4 = df_4.T

print(df_4)
df_4 = df_4.astype(int)
df_4.info()

# 스타일 서식 지정
plt.style.use('ggplot')

plt.plot(df_4)
plt.show()

# 판다스 방식 area
# alpha 투명도
# figsize 없으면 자동 생성
df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(12, 8))
plt.title('서울 -> 타도시', size=30)
plt.ylabel('이동 인구수', size=20)
plt.xlabel('기간', size=20)
plt.legend(fontsize=15)
plt.show()

# df_4.plot(kind='area', stacked=False, alpha=0.5)
# plt.show()


# 맷플롭립 방식
plt.figure(figsize=(12,6))
plt.stackplot(df_4.index, df_4.T, alpha=0.2, labels = df_4.columns)
plt.show()


# 판다스방식 + 객체를 받는 방식
ax = df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20,10))
ax.set_title('서울 -> 타도시', size=30, color='brown', weight='bold')
ax.set_ylabel('이동인구수', size=20, color='#003366')
ax.set_xlabel('기간', size=20, color='#4B0082')
ax.legend(fontsize=15)
plt.show()


# 맷플롭립 방식 + 객체를 받는 방식
fig, ax = plt.subplots(figsize=(20,10))
ax.stackplot(df_4.index, df_4.T, alpha=0.2, labels=df_4.columns)

ax.set_title('서울 -> 타도시', size=30, color='brown', weight='bold')
ax.set_ylabel('이동인구수', size=20, color='#003366')
ax.set_xlabel('기간', size=20, color='#4B0082')
ax.legend(fontsize=15)
plt.show()


# ====================================
df = pd.DataFrame({
    "A": [1, 3, 2, 4],
    "B": [4, 2, 3, 1],
    "C": [2, 3, 4, 5]
})

fig, axes = plt.subplots(2,2, figsize=(10,8))
