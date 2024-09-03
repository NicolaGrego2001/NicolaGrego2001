import os
import tarfile
from datetime import datetime

# Set the directory to backup and the backup directory
source_dir = '/path/to/source_directory'
backup_dir = '/path/to/backup_directory'

# Create a timestamped filename
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
backup_filename = os.path.join(backup_dir, f'backup_{timestamp}.tar.gz')

# Create a backup
with tarfile.open(backup_filename, 'w:gz') as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))

print(f"Backup created at {backup_filename}")
