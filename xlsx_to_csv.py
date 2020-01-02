import pandas as pd
import sys


if len(sys.argv) == 2:
    print("Error! CSV file not specified.")
    sys.exit(1)


data = pd.read_excel(sys.argv[1])
data.to_csv(
    sys.argv[2],
    encoding="utf-8",
    sep=",",
    float_format="%.2f",
    date_format="%d/%m/%Y",
    index=False,
)
print(0)
