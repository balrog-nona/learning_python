from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http  # HTTP object for signed requests
from oauth2client import file, client, tools  # for token storage
import re
import calendar_access

"""
This script counts how many kms I did on exercise bike counting from 27. 2. 2016 + creates an event on 28.2.2019 to 
my calendar with the total sum of kms.

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

# Call the Calendar API
start_point = "2016-02-27T10:00:00Z"  # in the format necesary according to the documentation
end_point = "2019-02-28T23:00:00Z"  # counting just until 28.2.2019
calendar_ID = calendar_access.ID  # calendar Cviceni
events_result = SERVICE.events().list(calendarId=calendar_ID, timeMax=end_point, timeMin=start_point,
                                      maxResults=10000, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

# processing event["description"] using regular expressions - counting total kms
initial_sum = 11585.0  # total kms up to start_point (27.2.2016)

def count_kms(iterable):
    """
    Function takes iterable of dicts, searches for number of kms in the description section of the event in each dict,
    cuts the word "km" and converts the string of kms into float.
    :param iterable: events from calendar
    :return: total count of kms in the whole history
    """
    part_count = 0
    pattern = '\d+[\.?\,?]?\d+?\s?[kK]'
    for item in iterable:
        if "rotoped" in item["summary"]:
            comment_string = re.sub(",", ".", item["description"])
            kms = re.search(pattern, comment_string).group().lower()
            kms = kms[:kms.find("k")]
            kms = float(kms.strip())
            part_count += kms
    return part_count + initial_sum

total = count_kms(events)

"""
# creating an event with the result - total kms
EVENT = {
    "summary": "rotoped soucet",
    "description": "{} km".format(total),
    "start": {"date": "2019-02-28"},
    "end": {"date": "2019-03-01"}
}

e = SERVICE.events().insert(calendarId=calendar_ID, body=EVENT).execute()  # notification can be made as well
"""
