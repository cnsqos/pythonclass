# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)

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

plt.style.use('ggplot')

df = pd.read_excel('data/남북한발전전력량 (2).xlsx')
print(df)

south = df.iloc[1:5, 2:]
south.index = ["수력","화력","원자력","신재생"]
print(south)

south_T = south.T
print(south_T)

plt.figure(figsize=(12,6))
sns.lineplot(data=south_T, marker="o", palette="pastel")
plt.show()

plt.title("남한 발전원별 전력 생산량 추이")
plt.xlabel("연도")
plt.ylabel("전력량 (억 kWh)")
plt.xticks(rotation=45)
plt.show()

