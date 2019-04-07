from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http  # HTTP object for signed requests
from oauth2client import file, client, tools  # for token storage
import re
import calendar_access
import datetime

"""
This script counts how many kms I did on exercise bike in my whole life using "rotoped soucet" event in my calendar + 
creates an event on the last day of every month to my calendar with the total sum of kms.

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

# creating dates to use in calling the calendar API
first_day = datetime.date.today().replace(day=1).isoformat()  # first day of the current month
last_day = datetime.date.today().isoformat()  # last day of the current month

# Calling the Calendar API
first_day = first_day + "T01:00:00Z"  # the format necessary according to the documentation
last_day = last_day + "T23:50:00Z"
calendar_ID = calendar_access.ID  # calendar Cviceni
events_result = SERVICE.events().list(calendarId=calendar_ID, timeMax=last_day, timeMin=first_day,
                                      maxResults=60, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])


def count_kms(iterable):
    """
    Function takes iterable of dicts, searches for number of kms in the description section of the event in each dict,
    cuts the word "km" and converts the string of kms into float.
    :param iterable: events from calendar
    :return: total count of kms for the current month
    """
    month_count = 0
    pattern = '\d+\.?\d+?\s?[kK]'
    for item in iterable:
        if "rotoped" in item["summary"] and "description" in item.keys():
            comment_string = re.sub(",", ".", item["description"])
            if re.search(pattern, comment_string):
                kms = re.search(pattern, comment_string).group().lower()
                kms = kms[:kms.find("k")]
                kms = float(kms.strip())
                # print(kms)
                month_count += kms
                # print(month_count)
    return month_count


this_month = count_kms(events)



total = this_month + sum_up_to_last_month

# creating an event with the result - total kms
next_month = datetime.date.today().month + 1  # type int
next_month_first_day = datetime.date.today().replace(month=next_month, day=1).isoformat()

EVENT = {
    "summary": "rotoped soucet",
    "description": "{} km".format(total),
    "start": {"date": datetime.date.today().isoformat()},
    "end": {"date": next_month_first_day}
}

e = SERVICE.events().insert(calendarId=calendar_ID, body=EVENT).execute()  # notification can be made as well
