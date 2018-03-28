import datetime

print(datetime.datetime(2003, 5, 12, 14, 33, 22, 245323))
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.fromordinal(5))
print(datetime.datetime.fromtimestamp(3635352))
print(datetime.datetime.utcfromtimestamp(3635352))
print()
d = datetime.date.today()
t = datetime.time(8, 23)
dt = datetime.datetime.combine(d, t)
print(dt)
print()

cdt = datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", "%A %d %B %Y, %H:%M:%S")
print(cdt)
print(cdt.date())
print(cdt.time())
print(cdt.day)
print(cdt.hour)
print(cdt.isoformat())