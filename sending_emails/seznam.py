import smtplib
import email_access

smtpObj = smtplib.SMTP_SSL('smtp.seznam.cz', 465)  # encrypted SSL protocol
smtpObj.set_debuglevel(True)
smtpObj.ehlo()  # chci kod 250

smtpObj.login(email_access.seznam['email'], email_access.seznam['password'])  # chci kod 235

smtpObj.sendmail(email_access.seznam['email'], email_access.gmail['email'], 'Subject: Hello\nDear Alice, '
                                                                           'so long and thank you for all the fish. '
                                                                           'Sincerely, Bob')

smtpObj.quit()  # chci kod 221 - session is ending

"""
Posilani seznam to seznam: email nema identifikovaneho odesilatele, nema predmet, vsechen text je v tele zpravy + email
je zarazen do spamu. Email prijde v normalnim case.

Posilani seznam to gmail: Email se mi objevi na seznamu jako nedorucitelna zprava Duvod:
5.0.0 smtp; 550-5.7.1 [2a02:598:a::78:89 11] Our system has detected that this message
Permanent Failure - Other or Undefined Status 
A to ackoli kod a message mezi servery vypadaji bez problemu. 
"""