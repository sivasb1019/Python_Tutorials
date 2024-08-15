import pandas as pd

df = pd.read_csv("Sample500.csv")
#print((df['Employee']).sample(20))
print(df.isnull().sum())
print()
df.Employee = df['Employee'].fillna('SB')
print(df)
print()
print(df.isnull().sum())
