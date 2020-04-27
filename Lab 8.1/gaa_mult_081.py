#!/usr/bin/env python3

class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

    def convert(self):
        return self.goals * 3 + self.points

    def __mul__(self, other):
        mul_goals = self.goals * other
        mul_points = self.points * other
        return Score(mul_goals, mul_points)

    def __rmul__(self, other):
        rmul_goals = self.goals * other
        rmul_points = self.points * other
        return Score(rmul_goals, rmul_points)

    def __imul__(self, other):
        mul = self * other
        self.goals, self.points = mul.goals, mul.points
        return self

    def __gt__(self, other):
        return self.convert() > other.convert()
