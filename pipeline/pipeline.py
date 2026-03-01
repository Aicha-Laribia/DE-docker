import sys
import pandas as pd
arguments =sys.argv
df=pd.DataFrame({"day": [1, 2], "numb_passenger": [3, 4]})
df["month"] = int(arguments[1])
print(df.head())
df.to_parquet(f"output_{arguments[1]}.parquet")
print("month:", arguments[1])