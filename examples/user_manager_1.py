import os
import subprocess
from datetime import datetime, timedelta

# Define the inactivity period (e.g., 30 days)
inactive_period = timedelta(days=30)

# Get the current date
current_date = datetime.now()

# List all users
users = subprocess.getoutput("cut -d: -f1 /etc/passwd").splitlines()

# Check each user
for user in users:
    # Get the last login time
    last_login = subprocess.getoutput(f"lastlog -u {user} | tail -n 1 | awk '{{print $4, $5, $8}}'")
    if 'in**' in last_login:
        print(f"{user} never actually logged in")
        continue
    print(f"{user} logged in in {last_login}")
    if last_login:
        last_login_date = datetime.strptime(last_login, '%b %d %Y')

        # Calculate the days since last login
        if (current_date - last_login_date) > inactive_period:
            # Disable the user
            os.system(f"# usermod -L {user}")
            print(f"User {user} has been disabled due to inactivity.")
