import smtplib
from email.mime.text import MIMEText

with smtplib.SMTP('smtp.next-cloud.it') as smtp_server:
    smtp_server.starttls()
    smtp_server.login('s.brazioli@next-data.com', 'password')

    msg = MIMEText("Hello, this is a test email.")
    msg['Subject'] = "Test Email"
    msg['From'] = 's.brazioli@next-data.com'
    msg['To'] = 's.brazioli@next-data.com'

    smtp_server.send_message(msg)
    print("Email sent successfully.")