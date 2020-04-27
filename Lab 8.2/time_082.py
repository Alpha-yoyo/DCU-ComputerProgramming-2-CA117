#!/usr/bin/env python3

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return 'The time is {:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

    def convert2seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def __eq__(self, other):
        return self.convert2seconds() == other.convert2seconds()

    def __gt__(self, other):
        return self.convert2seconds() > other.convert2seconds()

    def __add__(self, other):
        return self.seconds_to_time(self.convert2seconds() + other.convert2seconds())

    def __iadd__(self, other):
        add = self + other
        self.hour, self.minute, self.second = add.hour, add.minute, add.second
        return self

    @classmethod
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        return cls(hour, minute, second)
