import pandas as pd

df = pd.read_csv("people-100.csv")
print(df.head())
print((df['Name']).sample(10))
