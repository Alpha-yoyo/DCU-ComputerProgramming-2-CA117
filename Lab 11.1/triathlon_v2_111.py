#!/usr/bin/env python3

class Triathlon(object):
    def __init__(self):
        self.player = {}

    def add(self, other):
        self.player[other.name] = other

    def __str__(self):
        lis = []
        for k, v in sorted(self.player.items()):
            lis.append('Name: {}\nID: {}'.format(v.name, v.tid))
        return '\n'.join(lis)

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)
