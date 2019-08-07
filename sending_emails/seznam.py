import smtplib
import email_access
import OpenSSL

print('jdu na to')
smtpObj = smtplib.SMTP('smtp.seznam.cz', 465)
#smtpObj.set_debuglevel(1)
print('mam server')
# doma si zkusit pripojeni pres openssl - pozor na dlouhe pauzy

#context = OpenSSL.create_default_context()
#smtpObj.starttls(context=context)
print(smtpObj.starttls())  # ensuring the encryption
print('mam sifrovani')
print(smtpObj.ehlo())  # chci kod 250
print('mam ehlo')
print(smtpObj.login(email_access.seznam['email'], email_access.seznam['password']))  # chci kod 235

smtpObj.sendmail(email_access.seznam['email'], email_access.gmail['email'], 'Subject: Hello\nDear Alice, '
                                                                           'so long and thank you for all the fish. '
                                                                           'Sincerely, Fisheater')

print(smtpObj.quit())  # chci kod 221 - session is ending