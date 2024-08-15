import pandas as pd
marks = [10,27,18,19,8]
names = ["SB", "LS", "LL", "IV", "SV"]
df = pd.Series(marks, names)
print(df)
print(df.index)
print(df.values)
print(df.sort_values())
print(df.sort_index())
