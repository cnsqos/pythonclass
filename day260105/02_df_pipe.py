import pandas as pd

# 파일 로드
df = pd.read_csv('data/train.csv')

# 전체 출력
print("========== 전체 데이터 ===========")
print(df)
print()

# info 출력
print("=========== info ============")
print(df.info())
print()

# 필요한 컬럼만 선택
df = df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]

# 결측치 확인
print("=============== 결측치 확인 ============")
missing = df.isnull()
print(missing.sum())
print()

# Age 결측치 평균값으로 채우기
age_mean = df["Age"].mean()
df['Age'] = df['Age'].fillna(age_mean)

# Embarked 결측치 최빈값으로 채우기
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 성별을 숫자로 변환 (map 사용) {"male": 0, "female": 1}
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print("=========== 전처리 후 데이터 ===========")
print(df.head())
print()
print(df.describe())
print()
print(df.info())
print()

print("=========== 전처리 후 데이터 (함수화) ===========")

# 컬럼 선별 함수
def select_columns(df):
    return df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]

# Age 결측치 평균으로 채우기
def fill_age_mean(df):
    df = df.copy()
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

# Embarked 결측치 최빈값으로 채우기
def fill_embarked_mode(df):
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    return df

# 성별 맵핑 함수
def encode_sex(df):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df

df_clean = encode_sex(fill_embarked_mode(fill_age_mean(select_columns(df))))
df_clean.info()


print("========== pipe() 함수 사용 ===========")

df_clean2 = (
    df
    .pipe(select_columns)
    .pipe(fill_age_mean)
    .pipe(fill_embarked_mode)
    .pipe(encode_sex)
)

df_clean2.info()


print("========== pipe() 함수 추가작업 ===========")

def null_check(df, msg) :
    print(f"\n===== [{msg}] =====\n")
    print(df.head(3))
    print("\n결측치 개수\n")
    print(df.isnull().sum())
    return df

df_clean3 = (
    df
    .pipe(select_columns)
    .pipe(null_check, "컬럼 선택 후")
    .pipe(fill_age_mean)
    .pipe(null_check, "Age 결측 처리 후")
    .pipe(fill_embarked_mode)
    .pipe(null_check, "Embarked 결측 처리 후")
    .pipe(encode_sex)
)


df_clean3.info()