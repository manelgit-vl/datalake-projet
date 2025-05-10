import pandas as pd

# Met le bon chemin relatif ou absolu :
df = pd.read_parquet("datalake_project 2/Data_lake/gold/final_dataset")
print(df.head())
