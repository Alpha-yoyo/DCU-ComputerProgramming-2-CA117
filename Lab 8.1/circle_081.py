#!/usr/bin/env python3

class Point(object):
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, p2):
      return (self.x + p2.x) / 2, (self.y + p2.y) / 2

   def __str__(self):
      return('({:.1f}, {:.1f})'.format(self.x, self.y))

class Circle(object):
   def __init__(self, centre=(0, 0), radius=0):
      self.centre = centre
      self.radius = radius

   def __add__(self, other):
      return Circle(self.centre.midpoint(other.centre), self.radius + other.radius)

   def __str__(self):
      return 'Centre: {}\nRadius: {}'.format(self.centre, self.radius)
