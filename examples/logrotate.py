import os
import shutil
from datetime import datetime

# Log file path
logfile = "app.log"

# Create a timestamped backup of the current log file
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f"{logfile}.{timestamp}"

# Rename the log file
shutil.move(logfile, backup_file)

# Create a new empty log file
open(logfile, 'w').close()

print(f"Log file rotated. Backup created at {backup_file}")
