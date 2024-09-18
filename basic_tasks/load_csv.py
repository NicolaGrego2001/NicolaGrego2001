import csv

csv_object = []
with open('base.csv', 'rt') as in_csv:
    reader = csv.DictReader(in_csv)
    for record in reader:
        csv_object.append(record)


print(csv_object)
