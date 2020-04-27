#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    sports = {}

    def add_time(self, sport, time):
        Triathlete.sports[sport] = time
        self.time = sum(Triathlete.sports.values())

    def get_time(self, sport):
        return Triathlete.sports[sport]

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.time)
