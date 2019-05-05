#!/usr/bin/python3

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http  # HTTP object for signed requests
from oauth2client import file, client, tools  # for token storage
import re
import calendar_access
import making_date
import decimal


SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
CLIENT_SECRET = "/home/balrog/Dokumenty/Programování/doGIThubu/learning_python/cycling_calendar/counting_future/" \
                "client_secret.json"

store = file.Storage("storage.json")  # storing access token
credz = store.get()  # tries to get an access token with witch to make authorized API calls
if not credz or credz.invalid:  # if the credentials are missing or invalid
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)  # creates a valid access token
    credz = tools.run_flow(flow, store)  # storing this valid token

SERVICE = build("calendar", "v3", http=credz.authorize(Http()))  # creating an endpoint to that API; last par signes

# 1. call to the Calendar API - gathering events from this month to count
calendar_ID = calendar_access.ID  # calendar Cviceni
events_result = SERVICE.events().list(calendarId=calendar_ID, timeMax="2019-05-05T10:00:00Z",
                                      timeMin="2019-05-01T04:00:00Z", maxResults=6, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])  # type list

number = len(events)

# 2. creating an event
EVENT = {
    "summary": "rotoped soucet",
    "description": "{} km".format(number),
    "start": {"date": "2019-05-5"},
    "end": {"date": "2019-05-6"}
}

e = SERVICE.events().insert(calendarId=calendar_ID, body=EVENT).execute()  # notification can be made as well
