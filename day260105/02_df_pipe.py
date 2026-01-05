import pandas as pd

df = pd.read_csv('data/train.csv')

# df = 파일로드
# 전체출력
# 인포 출력
#  "Survived", "Pclass", "Sex", "Age", "Fare", "Embarked" 만 남기기
# 결측치확인
# Age 결측치 평균으로 채우기
# Embarked 결측치 최빈값으로 채우기
# 성별을 숫자로 변환 (map 사용) {"male": 0, "female": 1}

# 전체 출력
print("===== 전체 데이터 =====")
print(df)
print()

# 인포 출력
print("===== info =====")
print(df.info())
print()

#  "Survived", "Pclass", "Sex", "Age", "Fare", "Embarked" 만 남기기
df = df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]


# 결측치 확인
print("===== 결측치 확인 =====")
print(df.isnull().sum())
print()

# Age 결측치 → 평균값으로 채우기
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Embarked 결측치 → 최빈값으로 채우기
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 성별을 숫자로 변환 (map 사용)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 최종 결과 확인
print("===== 전처리 후 데이터 =====")
print(df.head())
print()

print("===== 최종 결측치 확인 =====")
print(df.isnull().sum())