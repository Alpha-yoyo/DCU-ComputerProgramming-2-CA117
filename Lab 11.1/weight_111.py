#!/usr/bin/env python3

class Weight(object):
    def __init__(self, pound=0, ounce=0):
        self.pound = pound
        self.ounce = ounce

    OUNCES_PER_POUND = 16

    def from_ounces(ounces):
        pound = ounces // 16
        ounce = ounces % 16
        return Weight(pound, ounce)

    def convert(self):
        return self.ounce + (self.pound * 16)

    def __add__(self, other):
        add_pound = self.pound + other.pound
        add_ounce = self.ounce + other.ounce
        return Weight(add_pound, add_ounce)

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()

    def __ge__(self, other):
        return self.convert() >= other.convert()

    def __iadd__(self, other):
        add = self + other
        self.pound, self.ounce = add.pound, add.ounce
        return self

    def __mul__(self, other):
        mul_pound = self.pound * other
        mul_ounce = self.ounce * other
        return Weight(mul_pound, mul_ounce)

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.pound, self.ounce)
