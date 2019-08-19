import smtplib
import email_access
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# creating message
sender = email_access.seznam['email']
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = sender
msg['Subject'] = 'Python email'
body = 'Hello,\nit was nice to meet you.\nSee you soon.'
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

# connecting to the server
smtpObj = smtplib.SMTP_SSL('smtp.seznam.cz', 465)  # encrypted SSL protocol
smtpObj.set_debuglevel(True)
smtpObj.ehlo()  # chci kod 250

smtpObj.login(email_access.seznam['email'], email_access.seznam['password'])  # chci kod 235

smtpObj.sendmail(sender, sender, text)  # from, to, message

smtpObj.quit()  # chci kod 221 - session is ending
