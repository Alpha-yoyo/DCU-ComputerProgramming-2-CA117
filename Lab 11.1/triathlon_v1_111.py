#!/usr/bin/env python3

class Triathlon(object):
    def __init__(self):
        self.player = {}

    def lookup(self, tid):
        if tid in self.player:
            return self.player[tid]
        return None

    def add(self, other):
        self.player[other.tid] = other

    def remove(self, other):
        del self.player[other]

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)
