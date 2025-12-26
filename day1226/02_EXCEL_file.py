# 확장프로그램 Excel Viewer 설치
# pip install openpyxl

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width',200)

df1 = pd.read_excel('data/남북한발전전력량.xlsx')
print(df1)

# df2 = 절대경로로 header=None 줘서 불러보기

df2 = pd.read_excel('C:\\pythonclass\\data\\남북한발전전력량.xlsx', header = None)
print(df2)
print()


