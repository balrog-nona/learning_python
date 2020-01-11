from datetime import date
from calendar import prevmonth, nextmonth, monthrange

"""
Creating dates to use in the FIRST call to the calendar API
timeMax must be the last day of last month.
timeMin must be the first day of last month because I will gather the events from the whole last month.
"""
last_month_year, last_month_number = prevmonth(year=date.today().year, month=date.today().month)
last_month = date.today().replace(year=last_month_year, month=last_month_number)  # object needed for monthrange
time_min1 = date.today().replace(day=1, month=last_month_number, year=last_month_year).isoformat() + "T01:00:00Z"

length_last_month = monthrange(last_month.year, last_month.month)[1]
time_max1 = date.today().replace(day=length_last_month, month=last_month_number, year=last_month_year).isoformat()
time_max1 += "T23:50:00Z"

"""
Creating dates to use in the SECOND call to the calendar API
I'm looking for the last event called "rotoped soucet" which was created last day penutimate month as a whole day event.
timeMin must be the last day of penultimate month.
timeMax must be the first day of the last month because that's how google calendar works - the whole day events end
the next day.
"""
penultimate_month_number = datetime.date.today().month - 2
penultimate_month = datetime.date.today().replace(month=penultimate_month_number)
length_penultimate_month = calendar.monthrange(penultimate_month.year, penultimate_month.month)[1]
time_min2 = datetime.date.today().replace(day=length_penultimate_month, month=penultimate_month_number).isoformat()
time_min2 = time_min2 + "T01:00:00Z"

time_max2 = datetime.date.today().replace(day=1, month=last_month_number).isoformat() + "T23:00:00Z"

"""
Creating dates for the new event
This event will be the whole day event which means:
start - the last day of last month
end - the first day of current month
"""

start_date = datetime.date.today().replace(day=length_last_month, month=last_month_number).isoformat()
end_date = datetime.date.today().replace(day=1).isoformat()
