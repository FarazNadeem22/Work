import pandas as pd 
import numpy as np 

df = pd.read_csv("file.csv")
df.head()

dict_ = {}
col_names = []
total = []

for i, col in enumerate(df.keys()):
   
    dict_[col] = [len(pd.unique(df[col])), len(df), df[col].isnull().sum(), df[col].min(), df[col].max()]
    total.append(len(df))
    col_names.append(col)   

unique_df = pd.DataFrame(dict_, columns=col_names, index=["Unique Values", "Total","No. Missinig Values","Min", "Max"])
unique_df = unique_df.T
unique_df
