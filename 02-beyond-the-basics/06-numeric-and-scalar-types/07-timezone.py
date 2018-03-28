import datetime

# python built-in timezones support is very basic. To have a more complete support, look for third-part modules

# although there are not many built-in timezones, datetime provides a timezone constructor, which can be used to
# create any timezone

cet = datetime.timezone(datetime.timedelta(hours=1), "CET")  # Central Europe Timezone
print(repr(cet))

# departure from norway
departure = datetime.datetime(year=2014, month=1, day=7, hour=11, minute=30, tzinfo=cet)
print(departure)
# arrival to london
arrival = datetime.datetime(year=2014, month=1, day=7, hour=13, minute=5, tzinfo=datetime.timezone.utc)
print(arrival)
print(arrival - departure)