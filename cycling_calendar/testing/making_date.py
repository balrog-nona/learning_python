import datetime
import calendar

"""
first_day = datetime.date.today().replace(day=1).isoformat()
first_day = first_day + "T01:00:00Z"

last_day = datetime.date.today().isoformat()
last_day = last_day + "T23:50:00Z"


next_month = datetime.date.today().month + 1
print(next_month, type(next_month))
next_month_first_day = datetime.date.today().replace(month=next_month, day=1).isoformat()
print(type(next_month_first_day))
"""

previous_month = datetime.date.today().month -1
this_day = datetime.date.today()
last_month = this_day.replace(month=previous_month)
print(calendar.monthrange(last_month.year, last_month.month))

print(last_month)

unor = datetime.date.today()
print(calendar.monthrange(unor.year, unor.month))