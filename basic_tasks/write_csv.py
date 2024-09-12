import csv

data = [
    {'name': 'Emily', 'surname': 'Johnson'},
    {'name': 'Michael', 'surname': 'Brown'},
    {'name': 'Olivia', 'surname': 'Williams'},
    {'name': 'James', 'surname': 'Davis'},
    {'name': 'Isabella', 'surname': 'Garcia'},
    {'name': 'Ethan', 'surname': 'Martinez'},
    {'name': 'Sophia', 'surname': 'Anderson'},
    {'name': 'Daniel', 'surname': 'Rodriguez'},
    {'name': 'Mia', 'surname': 'Thomas'},
    {'name': 'William', 'surname': 'Moore'}
]

# Filepath to save the CSV
simple_csv_filepath = 'base.csv'

# Create the CSV file with 10 records
with open(simple_csv_filepath, mode='wt') as out_csv:
    writer = csv.DictWriter(out_csv, ['name', 'surname'])
    writer.writeheader()
    writer.writerows(data)

