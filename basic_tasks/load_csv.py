import csv

with open('base.csv', 'rt') as in_csv:
    reader = csv.DictReader(in_csv)
    for record in reader:
        print(record)
