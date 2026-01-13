import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df)
print()

# 연비(mpg)와 차중(weight) 컬럼에 대한 산점도 그리기


# # 판다스 방식
# df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, marker='d', figsize=(10,5))
# plt.title('Scatter Plot - mpg vs. weight')
# plt.show()


# #맷플롯립 방식
# plt.figure(figsize=(10,5))
# plt.scatter(df['weight'],df['mpg'], c='green', s=10)
# plt.title('Scatter Plot - mpg vs. weight')
# plt.xlabel('weight')
# plt.ylabel('mpg')
# plt.show()


# sns 방식
# plt.figure(figsize=(10,5))
# sns.scatterplot(data=df, x='weight', y='mpg', hue='origin' ,color='coral', s=30, palette='Set2')
# plt.title('Scatter Plot - mpg vs. weight')
# plt.show()

# ================= 버블 차트 =================

print(df['cylinders'].unique())
cylinders_size = (df['cylinders'] / df['cylinders'].max()) * 300
print(cylinders_size)

df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10,5),
        s=cylinders_size, alpha=0.3)
plt.title('Scatter Plot - mpg vs weight - cylinders')
plt.show()


# ============ 저장하기 ============

df.plot(kind='scatter', x='weight', y='mpg', marker='+',
        cmap='rainbow', c=cylinders_size, s=50,
        figsize=(10,5),alpha=0.3)
# viridis, plasma, coolwarm, jet, rainbow
plt.title('Scatter Plot - mpg vs weight - cylinders')
plt.savefig('./data/scatter.png')
plt.savefig('./data/scatter_transparent.png', transparent=True)
plt.show()

