from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http  # HTTP object for signed requests
from oauth2client import file, client, tools  # for token storage
import re
import calendar_access
import making_date

"""
This script counts how many kms I did on exercise bike during a particular month + using "rotoped soucet" event in my 
calendar creates an event on the last day of every month to my calendar with the total sum of kms in my whole history.

The program will run every last day of the following months.

Video about authorization:
https://www.youtube.com/watch?v=h-gBeC9Y9cE

The substantial part of the code was taken from quickstart.py on the Google calendar API website.
"""

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
CLIENT_SECRET = "client_secret.json"

store = file.Storage("storage.json")  # storing access token
credz = store.get()  # tries to get an access token with witch to make authorized API calls
if not credz or credz.invalid:  # if the credentials are missing or invalid
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)  # creates a valid access token
    credz = tools.run_flow(flow, store)  # storing this valid token

SERVICE = build("calendar", "v3", http=credz.authorize(Http()))  # creating an endpoint to that API; last par signes

# 1. call to the Calendar API - gathering events from the current month to count
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
    month_count = 0
    pattern = '\d+\.?\d+?\s?[kK]'
    if iterable:
        for item in iterable:
            if "rotoped" in item["summary"] and "description" in item.keys():
                comment_string = re.sub(",", ".", item["description"])
                if re.search(pattern, comment_string):
                    kms = re.search(pattern, comment_string).group().lower()
                    kms = kms[:kms.find("k")]
                    kms = float(kms.strip())
                    month_count += kms
    return month_count


""""
Accessing the last event called "rotoped soucet" from previous month
This event has a start date last day of previous month and an end date first day of current month
"""
# 2. call to the calendar API - accessing event "rotoped soucet" from previous month
events_result2 = SERVICE.events().list(calendarId=calendar_ID, timeMax=making_date.time_max2,
                                       timeMin=making_date.time_min2, maxResults=6, singleEvents=True).execute()
events2 = events_result2.get('items', [])

for event in events2:
    if "rotoped soucet" in event["summary"]:
        sum_up_to_last_month = event["description"]
        sum_up_to_last_month = sum_up_to_last_month[:sum_up_to_last_month.find("k")]
        sum_up_to_last_month = float(sum_up_to_last_month.strip())

this_month = count_kms(events)
total = this_month + sum_up_to_last_month

# creating an event with the result - total kms
EVENT = {
    "summary": "rotoped soucet",
    "description": "{} km".format(total),
    "start": {"date": making_date.start_date},
    "end": {"date": making_date.end_date}
}

e = SERVICE.events().insert(calendarId=calendar_ID, body=EVENT).execute()  # notification can be made as well
