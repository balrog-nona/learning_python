#!/usr/bin/python3

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http  # HTTP object for signed requests
from oauth2client import file, client, tools  # for token storage
import re
import calendar_access
import making_date
from decimal import Decimal
from send_email import msg as msg
from send_email import smtpObj as smtpObj
from send_email import sender as sender
from email.mime.text import MIMEText
import pandas as pd
import altair as alt


"""
This script counts how many kms I did on exercise bike during a particular month + using "rotoped soucet" event in my 
calendar creates an event on the last day of every month to my calendar with the total sum of kms in my whole history.
After that, the script sends me an email with the result.

The program will run the first day of every month.

Video about authorization:
https://www.youtube.com/watch?v=h-gBeC9Y9cE

Google API documentation:
https://developers.google.com/api-client-library/python/
https://developers.google.com/calendar/v3/reference/events
https://developers.google.com/calendar/overview

The first 9 lines of the code was taken from quickstart.py on the Google calendar API website.
"""

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
CLIENT_SECRET = "/home/balrog/Dokumenty/Programování/doGIThubu/learning_python/cycling_calendar/counting_future/" \
                "client_secret.json"

store = file.Storage("storage.json")  # storing access token
credz = store.get()  # tries to get an access token with witch to make authorized API calls
if not credz or credz.invalid:  # if the credentials are missing or invalid
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)  # creates a valid access token
    credz = tools.run_flow(flow, store)  # storing this valid token

SERVICE = build("calendar", "v3", http=credz.authorize(Http()))  # creating an endpoint to that API; last par signes

# 1. call to the Calendar API - gathering events from the previous month to count
calendar_ID = calendar_access.ID  # calendar Cviceni
events_result = SERVICE.events().list(calendarId=calendar_ID, timeMax=making_date.time_max1,
                                      timeMin=making_date.time_min1, maxResults=60, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])  # type list


def count_kms(iterable):
    """
    Function takes iterable of dicts, searches for number of kms in the description section of the event in each dict,
    cuts the word "km" and converts the string of kms into float.
    :param iterable: events from calendar
    :return: total count of kms for the current month
    """
    month_count = Decimal("0.0")
    pattern = '\d+\.?\d+?\s?[kK]'
    if iterable:
        for item in iterable:
            if "rotoped" in item["summary"] and "description" in item.keys():
                comment_string = re.sub(",", ".", item["description"])
                if re.search(pattern, comment_string):
                    kms = re.search(pattern, comment_string).group().lower()
                    kms = kms[:kms.find("k")].strip()
                    month_count += Decimal(kms)
    return month_count


""""
Accessing the last event called "rotoped soucet" from the penultimate month
This event has a start date last day the penultimate month and an end date the first day of last month
"""
# 2. call to the calendar API - accessing event "rotoped soucet" from previous month
events_result2 = SERVICE.events().list(calendarId=calendar_ID, timeMax=making_date.time_max2,
                                       timeMin=making_date.time_min2, maxResults=6, singleEvents=True).execute()
events2 = events_result2.get('items', [])

for event in events2:
    if "rotoped soucet" in event["summary"]:
        sum_up_to_last_month = event["description"]
        sum_up_to_last_month = sum_up_to_last_month[:sum_up_to_last_month.find("k")].strip()
        sum_up_to_last_month = Decimal(sum_up_to_last_month)

this_month = count_kms(events)
total = this_month + sum_up_to_last_month

# creating an event with the result - total kms
EVENT = {
    "summary": "rotoped soucet",
    "description": "{} km".format(total),
    "start": {"date": making_date.start_date},
    "end": {"date": making_date.end_date}
}

e = SERVICE.events().insert(calendarId=calendar_ID, body=EVENT).execute()


# sending email with the result
body = 'Statistics:\nLast month: {} km\nTotal: {} km'.format(this_month, total)
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

smtpObj.sendmail(sender, sender, text)  # from, to, message

smtpObj.quit()


# print the table
with open('kms.csv', encoding='utf-8', mode='a') as file:
    file.write('{},{},{}\n'.format(making_date.start_date, this_month, total))

data_df = pd.read_csv('kms.csv')  # DataFrame object
print(data_df)


# data visualization
base = alt.Chart(data_df).properties(width=500)  # creating Chart object
line = base.mark_line(color='crimson').encode(x='date', y='kms')  # data visualization using Line Chart
rule = base.mark_rule(color='coral').encode(y='average(kms)', size=alt.value(2))  # line for average kms

my_chart = line + rule
my_chart.save('chart.png')
