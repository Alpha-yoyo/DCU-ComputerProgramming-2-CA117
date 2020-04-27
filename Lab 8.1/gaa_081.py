#!/usr/bin/env python

class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

    def convert(self):
        return self.goals * 3 + self.points

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __ne__(self, other):
        return self.convert() != other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __le__(self, other):
        return self.convert() <= other.convert()

    def __ge__(self, other):
        return self.convert() >= other.convert()

    def __add__(self, other):
        add_goals = self.goals + other.goals
        add_points = self.points + other.points
        return Score(add_goals, add_points)

    def __sub__(self, other):
        sub_goals = self.goals - other.points
        sub_points = self.points - other.points
        return Score(sub_goals, sub_points)

    def __iadd__(self, other):
        add = self + other
        self.goals, self.points = add.goals, add.points
        return self

    def __isub__(self, other):
        sub = self - other
        self.goals, self.points = sub.goals, sub.points
        return self
