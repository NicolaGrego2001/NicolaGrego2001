import csv

# Data for the CSV
data = [
    ["Emily", "Johnson"],
    ["Michael", "Brown"],
    ["Olivia", "Williams"],
    ["James", "Davis"],
    ["Isabella", "Garcia"],
    ["Ethan", "Martinez"],
    ["Sophia", "Anderson"],
    ["Daniel", "Rodriguez"],
    ["Mia", "Thomas"],
    ["William", "Moore"]
]

# Filepath to save the CSV
simple_csv_filepath = 'base.csv'

# Create the CSV file with 10 records
with open(simple_csv_filepath, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['name', 'surname'])

    # Write data
    writer.writerows(data)