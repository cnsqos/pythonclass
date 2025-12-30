import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red'],
    'size': ['S', 'M', 'L', 'S'],
    'shape': ['circle', 'square', 'triangle', 'circle']
})

print(data)
print()

encoder = OneHotEncoder(sparse_output=False)
print(data.ndim)
print()

encoded = encoder.fit_transform(data) # 2차원 인풋 기대

print(encoded)
print()


print(data.columns)
print()


encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(data.columns)
)

# encoded_df = pd.DataFrame(
#     encoded,
#     columns=['blue','green','red','L','M','S','circle','square','triangle']
# )
print(encoded_df)


