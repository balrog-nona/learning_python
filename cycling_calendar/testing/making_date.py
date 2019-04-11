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

"""
day_one = datetime.date.today().replace(day=1)
previous_month_number = datetime.date.today().month -1
last_month = this_day.replace(month=previous_month)
last_day = calendar.monthrange(previous_month.year, previous_month.month)[1]
"""

last_month_number = datetime.date.today().month - 1
last_month = datetime.date.today().replace(day=1, month=last_month_number)
last_day_previous_month = calendar.monthrange(last_month.year, last_month.month)[1]
print(last_day_previous_month)
