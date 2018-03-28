# Iterables - Reading data from a sensor
# Often sensors produce stream of data or can simply provide a value whenever queried

import random
import datetime
import itertools
import time


class Sensor:
    """
    Simulates a physical sensor
    """
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


sensor = Sensor()
timestamps = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, value)
    time.sleep(1)


# TODO: Make Sensor class return CPU temperature
