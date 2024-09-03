import shutil
import smtplib
from email.mime.text import MIMEText

# Set the threshold (e.g., 80% usage)
threshold = 80

# Get disk usage
total, used, free = shutil.disk_usage("/")

# Calculate the percentage of disk used
percent_used = (used / total) * 100

# Check if the usage exceeds the threshold
if percent_used > threshold:
    # Send email alert
    msg = MIMEText(f"Warning: Disk usage is at {percent_used:.2f}%")
    msg['Subject'] = 'Disk Space Alert'
    msg['From'] = 's.brazioli@next-data.com'
    msg['To'] = 's.brazioli@next-data.com'

    with smtplib.SMTP('smtp.next-cloud.it') as server:
        server.login("s.brazioli@next-data.com", "password")
        server.send_message(msg)
    print("Disk space alert sent.")
else:
    print(f"Disk space usage is {percent_used:.2f}%. All good.")
