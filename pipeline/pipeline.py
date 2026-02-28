import sys
import pandas as pd
arguments =sys.argv
df=pd.DataFrame({"day": [1, 2], "numb_passenger": [3, 4]})
df["month"] = int(arguments[1])
print(df.head())
print("month:", int(arguments[1]))
