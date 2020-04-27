#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def less_than(self, other):
        total1 = self.goals * 3 + self.points
        total2 = other.goals * 3 + other.points
        return total1 < total2

    def greater_than(self, other):
        total1 = self.goals * 3 + self.points
        total2 = other.goals * 3 + other.points
        return total1 > total2

    def equal_to(self, other):
        total1 = self.goals * 3 + self.points
        total2 = other.goals * 3 + other.points
        return total1 == total2
