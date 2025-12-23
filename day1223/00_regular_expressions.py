# 정규 표현식(regular expressions)

data = """
park 800905-1049118
kim 700905-1059119
"""

# park 8800905-********
# park 7000905-********

for line in data.split("\n"):
    print(line)


print('123'.isdigit()) #
print('a123'.isdigit()) #

words = ['apple', 'banana', 'mango']
print(" ".join(words))


print()