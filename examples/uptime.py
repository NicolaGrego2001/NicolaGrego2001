import subprocess
import smtplib
from email.mime.text import MIMEText

# Set the maximum uptime in seconds (e.g., 30 days)
max_uptime = 30 * 24 * 60 * 60

# Check the uptime
uptime_seconds = float(subprocess.getoutput("cat /proc/uptime").split()[0])

if uptime_seconds > max_uptime:
    # Send email alert
    msg = MIMEText(f"Warning: System uptime is {uptime_seconds / 86400:.2f} days.")
    msg['Subject'] = 'System Uptime Alert'
    msg['From'] = 's.brazioli@next-data.com'
    msg['To'] = 's.brazioli@next-data.com'

    with smtplib.SMTP('smtp.next-cloud.it') as smtp_server:
        smtp_server.starttls()
        smtp_server.login('s.brazioli@next-data.com', 'password')
        smtp_server.send_message(msg)
    print("Uptime alert sent.")
else:
    print(f"System uptime is {uptime_seconds / 86400:.2f} days. No action needed.")
