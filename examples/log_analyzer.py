import time
import smtplib
from email.mime.text import MIMEText

# Log file to monitor
logfile = "/var/log/syslog"

# Keywords to look for
keywords = ["error", "failed", "critical"]

def send_email_alert(keyword, line):
    msg = MIMEText(f"Alert: {keyword} found in log:\n\n{line}")
    msg['Subject'] = f"Log Alert: {keyword}"
    msg['From'] = 'admin@example.com'
    msg['To'] = 'user@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("admin@example.com", "password")
        server.send_message(msg)
    print("Alert email sent.")

# Open the log file and monitor it
with open(logfile, "r") as f:
    f.seek(0, 2)  # Move to the end of the file

    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        for keyword in keywords:
            if keyword in line.lower():
                send_email_alert(keyword, line)
