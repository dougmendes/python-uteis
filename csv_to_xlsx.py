import csv
import numpy
import pandas
import sys


csv = numpy.loadtxt(
    "\\Users\BI001607\Desktop\CSVXLSX\Extrato.csv", delimiter=";", dtype=str, skiprows=5
)
df = pandas.DataFrame(csv)
df.to_excel(f"{sys.argv[1]}.xlsx", header=False, index=False)
