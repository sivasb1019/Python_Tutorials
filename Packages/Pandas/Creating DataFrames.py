import pandas as pd
import numpy as np

dict1 = {"Cars":["Benz","Audi","Porsche"],
         "Year":[27,10,19]}
print("Dictionary 1:",dict1)

df = pd.DataFrame(dict1,index=[1,2,3])
print(df)

df = pd.DataFrame(np.arange(0,10).reshape(5,2), index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2"])
print(df)
df.to_csv("eg.csv")
