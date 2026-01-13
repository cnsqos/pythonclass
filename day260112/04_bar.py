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


# 전출지 = 서울, 전입지 = 서울빼고(전국) ==> 서울을 나간 사람들 (네덜란드튤립농장 - 순정)

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

# ===========================================

# 스타일 지정

plt.style.use('Solarize_Light2')


# 막대 그래프 그리기

df_4.plot(kind= 'bar', figsize=(16,8), width=0.5, color=['orange','green','skyblue','blue'])

plt.title('서울 -> 타시도 인구 이동', pad=10, size=30, fontweight='bold', color='brown')
plt.ylabel('이동 인구수', labelpad=10, size=20)
plt.xlabel('기간', labelpad=10, size=20)

plt.show()

