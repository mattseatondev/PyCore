import pandas as pd

from Challenges.util import pr

data = [
    {"user_id": 1, "name": "Alice", "age": 25, "score": 88},
    {"user_id": 2, "name": "Bob", "age": 30, "score": 95},
    {"user_id": 3, "name": "Charlie", "age": 22, "score": 70},
    {"user_id": 4, "name": "Dana", "age": 28, "score": 82},
]

df = pd.DataFrame(data)
# pr(df)
# pr(df[df['age'] > 25])
# pr(df.sort_values(by='score', ascending=False))
df['passed'] = df['score'] >= 80
# pr(df)
# pr(df.groupby('passed')['score'].mean())
# pr(df.groupby('passed')['score'].agg(['mean', 'max']))

# Applying functions to dataframes
df['name_len'] = df['name'].apply(len)
df['name_plus_score'] = df.apply(lambda row: row['age'] + row['score'], axis=1)

# df['age'].fillna(df['age'].mean(), inplace=True)

df2 = pd.DataFrame([{"user_id": 1, "city": "NY"}, {"user_id": 2, "city": "LA"}])
merged = pd.merge(df, df2, on='user_id', how='left')

print(merged)

# Large DataFrames
# pd.read_csv('file.csv', chunksize=1000)
# astype()
# Vectorized