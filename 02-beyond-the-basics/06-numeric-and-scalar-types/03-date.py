import datetime
# representing dates not caring about the time
print(datetime.date(2014, 1, 6))
print(datetime.date(year=2014, month=1, day=6))
print()
# some factory methods
print(datetime.date.today())
print(datetime.date.fromtimestamp(1000000000))
print(datetime.date.fromordinal(1))
print(datetime.date.fromordinal(365))
print()
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)
print()
d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)
print()
# weekday - (MON-SUN)    -> 0-6
print(d.weekday())
# isoweekday - (MON-SUN) -> 1-7
print(d.isoweekday())
# representation of date and time (ISO 8601:2004)
print(d.isoformat())
print()
# date formating relies on the operating system where python runtime is running. So, it is not portable
print(d.strftime('%A %d %B %y'))
print('The date is {:%A %d %B %y}'.format(d))

e = datetime.date(2014, 1, 6)
# -d (depending on the OS, removes leading zeroes from the day
print(e.strftime('%A %-d %B %y'))
print('{date:%A} {date.day} {date:%B} {date.year}'.format(date=e))
print()
print(datetime.timedelta(1))