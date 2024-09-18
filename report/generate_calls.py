import csv
import random
from datetime import datetime, timedelta

# Number of records to generate
num_records = 1_000_000

# Random 10 caller numbers
caller_numbers = [f"+12345678{str(i).zfill(2)}" for i in range(10)]

# Random 100 recipient numbers
recipient_numbers = [f"+98765432{str(i).zfill(3)}" for i in range(100)]

# Random date generation between the past year and now
start_date = datetime.now() - timedelta(days=365)

# Filepath to save the CSV
filepath = 'calls.csv'

# Create the CSV file with 1,000,000 records
with open(filepath, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['caller_number', 'recipient_number', 'call_start_time', 'call_duration_sec'])

    for _ in range(num_records):
        # Randomly choose a caller and recipient number
        caller = random.choice(caller_numbers)
        recipient = random.choice(recipient_numbers)

        # Generate random call start time
        call_start_time = start_date + timedelta(seconds=random.randint(0, 365 * 24 * 60 * 60))

        # Random call duration between 10 seconds and 2 hours (7200 seconds)
        call_duration = random.randint(10, 7200)

        # Write the record to the CSV
        writer.writerow([caller, recipient, call_start_time.strftime('%Y-%m-%d %H:%M:%S'), call_duration])