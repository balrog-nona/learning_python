import smtplib
import email_access
from email.mime.multipart import MIMEMultipart

# creating message
sender = email_access.seznam['email']
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = sender
msg['Subject'] = 'Exercise bike last month'

# connecting to the server
smtpObj = smtplib.SMTP_SSL('smtp.seznam.cz', 465)  # encrypted SSL protocol
smtpObj.ehlo()

smtpObj.login(email_access.seznam['email'], email_access.seznam['password'])