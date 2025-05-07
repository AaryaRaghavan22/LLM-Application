import pandas as pd
df = pd.read_csv("Clothing review.csv")
print(df.head())  # show the first few rows
print(df.columns)  # check column names
print(df["Review Text"].isna().sum())