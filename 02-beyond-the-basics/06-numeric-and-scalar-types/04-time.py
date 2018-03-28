import datetime
# representing time not caring about the date
print(datetime.time(3))
print(datetime.time(3, 1))
print(datetime.time(3, 1, 2))
print(datetime.time(3, 1, 2, 232))  # the last parameter is microseconds
t = datetime.time(hour=23, minute=59, second=59, microsecond=999999)
print()
print('hour={time.hour}, minute={time.minute}, second={time.second}, microsecond={time.microsecond}'.format(time=t))
print(t)
print(t.isoformat())
print()
# the formatting below depends on the OS
print(t.strftime('%Hh%Mm%Ss'))
# prefer this more pythonic approach instead
print('{time.hour}h{time.minute}m{time.second}s'.format(time=t))
print()
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)