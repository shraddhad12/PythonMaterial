import pandas as pd
import csv

with open("test.csv", "r") as r:
    reader = csv.reader(r)
    rows = list(reader)

with open("test.csv", 'w') as row:
    writer = csv.writer(row)
    header = []
    with open('header.txt', 'r') as file:
        for line in file:
            header.append(line)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)

df = pd.read_csv("test.csv", index_col=False)
print(df)