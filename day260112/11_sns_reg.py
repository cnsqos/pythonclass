# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# plt.style.use('ggplot')
sns.set_style('darkgrid')

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


titanic = sns.load_dataset('titanic')

print(titanic.head())
print()

fig, axes = plt.subplots(1,2, figsize=(15,5))

sns.regplot(data=titanic, x='age', y='fare', ax=axes[0])
axes[0].set_title("regplot : 회귀선 + 신뢰구간")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Fare")
axes[0].set_ylim(0, 300)


sns.regplot(data=titanic, x='age', y='fare', ax=axes[1], fit_reg=False)
axes[1].set_title("regplot : 회귀선 + 신뢰구간")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Fare")
axes[1].set_ylim(0, 300)

plt.show()

