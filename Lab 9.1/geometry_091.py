#!/usr/bin/env python3

class Shape(object):
    def __init__(self, points):
        self.points = points

    def sides(self):
        return [self.points[x].distance(self.points[x - 1]) for x in range(-2, len(self.points) - 2)]

    def perimeter(self):
        return sum(self.sides())

class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Triangle(Shape):
    def area(self):
        s = self.perimeter() / 2
        a, b, c = self.sides()
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Square(Shape):
    def area(self):
        width = self.sides()[0]
        length = self.sides()[1]
        return width * length
