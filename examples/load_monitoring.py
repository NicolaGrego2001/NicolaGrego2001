import os
import smtplib
from email.mime.text import MIMEText
import psutil

# Set load threshold (e.g., 5 minutes average load > 2.0)
load_threshold = 2.0

# Get system load averages
load1, load5, load15 = os.getloadavg()

# Check if 5-minute load average exceeds threshold
if load5 > load_threshold:
    # Send email alert
    msg = MIMEText(f"High system load detected: 5-minute average load is {load5}")
    msg['Subject'] = 'System Load Alert'
    msg['From'] = 's.brazioli@next-data.com'
    msg['To'] = 's.brazioli@next-data.com'

    with smtplib.SMTP('smtp.next-data.com') as smtp_server:
        smtp_server.starttls()
        smtp_server.login('s.brazioli@next-data.com', 'password')
        smtp_server.send_message(msg)

    print("System load alert sent.")
else:
    print(f"System load is normal. 5-minute average load is {load5}")
