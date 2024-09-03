import os
import shutil
import time

# Directory containing log files
log_directory = "myapp/"

# Directory to move archived logs
archive_directory = "myapp/archive/"

# Number of days before logs are archived
days_old = 30

# Create the archive directory if it doesn't exist
if not os.path.exists(archive_directory):
    os.makedirs(archive_directory)

# Current time in seconds
current_time = time.time()

# Archive old log files
for filename in os.listdir(log_directory):
    filepath = os.path.join(log_directory, filename)

    # Only archive files older than `days_old`
    if os.stat(filepath).st_mtime < (current_time - days_old * 86400):
        shutil.move(filepath, os.path.join(archive_directory, filename))
        print(f"Archived {filename}")
