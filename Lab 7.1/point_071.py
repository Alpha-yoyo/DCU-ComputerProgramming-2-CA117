#!/usr/bin/env python3

import math

class Point(object):

    def __init__(self, pointx=0, pointy=0):
        self.pointx = pointx
        self.pointy = pointy

    def distance(self, other):
        return math.sqrt((other.pointx - self.pointx) ** 2 + (other.pointy - self.pointy) ** 2)

    def reflect(self):
        self.pointx *= -1
        self.pointy *= -1
