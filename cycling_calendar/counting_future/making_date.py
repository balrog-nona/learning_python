from datetime import date
from calendar import monthrange
from dateutil.relativedelta import relativedelta

"""
Creating dates to use in the FIRST call to the calendar API
timeMin1 must be the first day of last month because I will gather the events from the whole last month.
timeMax1 must be the last day of last month.
"""
last_month = date.today() - relativedelta(months=1)  # date object
time_min1 = date.today().replace(day=1, month=last_month.month, year=last_month.year).isoformat() + "T01:00:00Z"

length_last_month = monthrange(last_month.year, last_month.month)[1]
time_max1 = date.today().replace(day=length_last_month, month=last_month.month, year=last_month.year).isoformat()
time_max1 += "T23:50:00Z"

"""
Creating dates to use in the SECOND call to the calendar API
I'm looking for the last event called "rotoped soucet" which was created last day penutimate month as a whole day event.
timeMin2 must be the last day of penultimate month.
timeMax2 must be the first day of the last month because that's how google calendar works - the whole day events end
the next day.
"""
penultimate_month = date.today() - relativedelta(months=2)  # date object
length_penultimate_month = monthrange(penultimate_month.year, penultimate_month.month)[1]
time_min2 = date.today().replace(day=length_penultimate_month, month=penultimate_month.month,
                                 year=penultimate_month.year).isoformat()
time_min2 = time_min2 + "T01:00:00Z"

time_max2 = date.today().replace(day=1, month=last_month.month, year=last_month.year).isoformat() + "T23:00:00Z"

"""
Creating dates for the new event
This event will be the whole day event which means:
start - the last day of last month
end - the first day of current month
"""
start_date = date.today().replace(day=length_last_month, month=last_month_number, year=last_month_year).isoformat()
end_date = date.today().replace(day=1).isoformat()
