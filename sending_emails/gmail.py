import smtplib  # modul pro posilani mejlu
import email_access

"""
Abych se dostala ke svemu mejlu, musela jsem si zapnout povoleni less secure apps. To
povoleni jsem pak vypla, cili kod nize bez opetovneho zapnuti nebude fungovat.
"""

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)  # 587 - TLS encryption
print(type(smtpObj))

print(smtpObj.ehlo()) # establishing connection to the server, firste step after having SMTP object
# 250 is code of success in smtplib

# next step: calling starttls() for ensuring the encryption
print(smtpObj.starttls())  # 220 = encrypted connection is set up

# login
print(smtpObj.login(email_access.gmail_email, email_access.gmail_password))  # kod 235 - accepted

smtpObj.sendmail(email_access.gmail_email, email_access.gmail_email, 'Subject: So long\nDear Alice, so long and thank '
                                                                     'you for all the fish. Sincerely, Bob')

# funguje! sendmail ma return value dictionary - prazdny slovnik znamena, ze vsichni adresati email obdrzeli

print(smtpObj.quit())  # 221 - session is ending

"""
neprochazela jsem cast lekce o IMAP, protoze v dohledne dobe nemam v planu si mejly stahovat
"""