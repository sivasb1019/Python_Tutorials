import pandas as pd

df = pd.read_csv("Sample500.csv")
print(df.groupby(by='Sex').size())
print(df['Value'].agg(['min','max','mean']))
print()
print(df[df.Sex=='Male'])
print("______________________")
print(df.sort_values(by='Leave').head())
