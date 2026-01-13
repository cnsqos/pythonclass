import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plt.style.use('gg')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df)
print()

df['count'] = 1
print(df)
print()

df_origin = df.groupby('origin').sum(numeric_only=True)
print(df_origin)
print()


df_origin.index = ['USA','EU', 'JAPAN']
print(df_origin)
print()

df_origin['count'].plot(kind='pie', figsize=(7,5), autopct='%1.1f%%',
                        startangle=90,
                        colors=['chocolate','bisque','cadetblue'],
                        textprops={'fontsize':14})
plt.title('Model Origin',size=20)
plt.axis('equal')
plt.legend(labels=df_origin.index)
plt.show()

