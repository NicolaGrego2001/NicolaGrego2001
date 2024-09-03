import os
import time
from datetime import datetime, timedelta

# Schedule the reboot for Sunday at 2 AM
reboot_time = "02:00"

while True:
    now = datetime.now()
    if now.strftime('%H:%M') == reboot_time and now.weekday() == 6:  # Sunday
        print("Scheduled reboot time reached. Rebooting...")
        os.system("# reboot")

    time.sleep(60)  # Check every minute