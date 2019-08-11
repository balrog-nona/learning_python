import smtplib  # modul pro posilani mejlu
import email_access

"""
Abych se dostala ke svemu mejlu, musela jsem si zapnout povoleni less secure apps. To
povoleni jsem pak vypla, cili kod nize bez opetovneho zapnuti nebude fungovat.
"""

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(type(smtpObj))

smtpObj.set_debuglevel(True)


smtpObj.ehlo()  # establishing connection to the server, first step after having SMTP object
# 250 is code of success in smtplib

# login
smtpObj.login(email_access.gmail['email'], email_access.gmail['password'])  # kod 235 - accepted

# nejdriv email odesilatele, pak email prijemce
smtpObj.sendmail(email_access.gmail['email'], email_access.gmail['email'], 'Subject: So long\nDear Alice, '
                                                                           'so long and thank you for all the fish. '
                                                                           'Sincerely, Bob')

# sendmail ma return value dictionary - prazdny slovnik znamena, ze vsichni adresati email obdrzeli

smtpObj.quit()  # 221 - session is ending

"""
Funguje perfektne posilani gmail to gmail a gmail to seznam. Email je identifikovany jako poslany mnou, ma predmet
a telo emailu. Prijde v normalnim case.
"""