"""Counts the amount of lines of the specified XLSX file.
"""

import pandas as pd
import sys


if len(sys.argv) == 1:
    print("Error! XLSX file not specified.")
    sys.exit(1)

try:
    xlsx = pd.read_excel(f"{sys.argv[1]}.xlsx")
    print(len(xlsx))

except IOError:
    print("XLSX file not found: {}".format(sys.argv[1]))
    sys.exit(1)
