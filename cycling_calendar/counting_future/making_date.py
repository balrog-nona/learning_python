import datetime
import calendar

"""
Creating dates to use in the FIRST call to the calendar API
timeMax must be the last day of current month - which means the day of running the program.
timeMin must be the first day of current month because I will gather the events from the whole current month.
"""
time_min1 = datetime.date.today().replace(day=1).isoformat()
time_max1 = datetime.date.today().isoformat()

# the format necessary according to the documentation
time_min1 = time_min1 + "T01:00:00Z"
time_max1 = time_max1 + "T23:50:00Z"

"""
Creating dates to use in the SECOND call to the calendar API
I'm looking for the last event called "rotoped soucet" which was created the previous month as a whole day event.
timeMin must be the last day of last month.
timeMax must be the first day of the current month because that's how google calendar works - the whole day events ends
the next day.
"""
last_month_number = datetime.date.today().month - 1
last_month = datetime.date.today().replace(day=1, month=last_month_number)
# the day must be set to 1 because every month has day 1, but not every has day 31
last_day = calendar.monthrange(last_month.year, last_month.month)[1]
time_min2 = datetime.date.today().replace(day=last_day, month=last_month_number).isoformat()
time_min2 = time_min2 + "T01:00:00Z"

time_max2 = datetime.date.today().replace(day=1).isoformat() + "T23:00:00Z"

"""
Creating dates for the new event
This event will be the whole day event which means:
start must be today - last day of current month
end must be tomorrow - the first day of next month
"""

start_date = datetime.date.today().isoformat()
next_month_number = datetime.date.today().month + 1  # type int
end_date = datetime.date.today().replace(day=1, month=next_month_number).isoformat()
