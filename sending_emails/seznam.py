import smtplib

smtpObj = smtplib.SMTP('smtp.seznam.cz', 465)

print(smtpObj.ehlo())  # chci kod 250

print(smtpObj.starttls())  # ensuring the encryption

print(smtpObj.login(email_access.seznam['email'], email_access.seznam['password']))  # chci kod 235

smtpObj.sendmail(email_access.seznam['email'], email_access.gmail['email'], 'Subject: Hello\nDear Alice, '
                                                                           'so long and thank you for all the fish. '
                                                                           'Sincerely, Fisheater')

print(smtpObj.quit())  # chci kod 221 - session is ending