"""Counts the amount of lines of the specified CSV file.
"""

import csv
import sys


if len(sys.argv) == 1:
    print("Error! CSV file not specified.")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as input_file:
        csv_file = csv.reader(input_file)
        line_count = len(list(csv_file))

    print(line_count)

except IOError:
    print("CSV file not found: {}".format(sys.argv[1]))
    sys.exit(1)
