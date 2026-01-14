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

sns.scatterplot(data=titanic, x='age', y='fare', hue='sex', style='sex', markers={'male':'o','female':'d'}, palette={'male':'steelblue', 'female':'tomato'}, size='pclass', sizes=(20,120), alpha=0.5, ax=axes[0])

axes[0].set_title("scatterplot: hue+style+size")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Fare")
axes[0].set_ylim(0, 300)
axes[0].legend(title="sex / pclass", loc="upper right")


# 생존별 나이/요금 산점도 그래프

sns.scatterplot(
    data=titanic,
    x="age", y="fare",
    hue="survived",
    palette="Set2",
    alpha=0.45,
    size=70,
    ax=axes[1]
)
axes[1].set_title("scatterplot: hue=survived")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("")
axes[1].set_ylim(0, 300)
axes[1].legend(title="survived", loc="upper right")


plt.show()

