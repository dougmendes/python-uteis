import pandas as pd
import sys
from datetime import datetime

df = pd.read_excel("/Users/bi001607/Desktop/"+sys.argv[1], header=1, dtype=str)

df.loc[:, sys.argv[2]] = [item.zfill(11) if len(item) <= 11 else item.zfill(14) for item in df[sys.argv[2]]]

df.to_csv(sys.argv[3],index = False)

