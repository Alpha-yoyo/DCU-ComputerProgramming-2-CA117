#!/usr/bin/env python3

class Triathlon(object):
    def __init__(self):
        self.player = {}

    def add(self, other):
        self.player[other.time] = other

    def best(self):
        return self.player[min(self.player.keys())]

    def worst(self):
        return self.player[max(self.player.keys())]

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    sports = {}

    def add_time(self, sport, time):
        Triathlete.sports[sport] = time
        self.time = sum(Triathlete.sports.values())

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.time)
