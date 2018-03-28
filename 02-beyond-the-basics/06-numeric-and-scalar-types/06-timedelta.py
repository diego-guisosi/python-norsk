import datetime

# timedelta accepts and sums:
#       days
#       seconds
#       microseconds
#       milliseconds
#       minutes
#       hours
#       weeks
#
# the result only stores: days, seconds, microseconds

print(datetime.timedelta(milliseconds=1, microseconds=1000))
td = datetime.timedelta(weeks=1, minutes=2, milliseconds=5500)
print(td.days)
print(td.seconds)
print(td.microseconds)
print()
print(td)
print("{!r}".format(td))  # !r forces format to use repr() instead of str()
print()
a = datetime.datetime(year=2014, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2014, month=3, day=14, hour=12, minute=9)
c = a - b
print(c)  # results in a timedelta
print(c.total_seconds())
print()
# it is also possible to sum date with timedeltas that have only date values
print(datetime.date.today() + datetime.timedelta(weeks=1) * 3)  # summing 3 weeks