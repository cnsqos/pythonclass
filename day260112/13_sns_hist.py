# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig, axes = plt.subplot_mosaic([['top_left','top_right'],['middle_left','middle_right'],['bottom','bottom']],figsize=(15,6),
                         constrained_layout=True) # 간격 최대한 조정 옵션

sns.histplot(data=titanic, x='age', bins=10, ax=axes['top_left'])

sns.histplot(x='age', hue='survived', data=titanic, bins=10, alpha=0.4, ax=axes['top_right']) # multiple='layer' 디폴트 값

sns.histplot(x='age', hue='survived', multiple='dodge', data=titanic, palette='muted', ax=axes['middle_left']) # multiple = 'dodge' 그래프 나란히

sns.histplot(x='age', hue='survived', multiple='stack', data=titanic, ax=axes['middle_right'])

sns.histplot(x='age', hue='survived', multiple='fill', bins=10, data=titanic, ax=axes['bottom'])

axes['top_left'].set_title("Histogram")
axes['top_right'].set_title("Histogram (hue)")
axes['top_left'].set_title("Histogram (multiple - dodge)")
axes['top_right'].set_title("Histogram (multiple - stack)")
axes['bottom'].set_title("Histogram (multiple - fill)")

plt.show()


