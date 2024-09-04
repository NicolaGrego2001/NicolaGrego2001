import smtplib
from email.mime.text import MIMEText

with open('/tmp/password.txt', 'rt') as in_password:
    password = in_password.read().splitlines()[0]
username = 's.brazioli@next-data.com'

with smtplib.SMTP_SSL('smtp.next-cloud.it', 465) as smtp_server:
    smtp_server.login(username, password)

    msg = MIMEText("Hello, this is a test email.")
    msg['Subject'] = "Test Email"
    msg['From'] = 's.brazioli@next-data.com'
    msg['To'] = 'administrator@brazioli.com'

    smtp_server.send_message(msg)
    print("Email sent successfully.")
