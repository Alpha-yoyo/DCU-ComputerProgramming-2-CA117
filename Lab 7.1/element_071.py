#!/usr/bin/env python3

class Element(object):

   def __init__(self, number, name, symbol, boiling):
      self.number = number
      self.name = name
      self.symbol = symbol
      self.boiling = boiling

   def print_details(self):
      print("Number: {:d}".format(self.number))
      print("Name: {:s}".format(self.name))
      print("Symbol: {:s}".format(self.symbol))
      print("Boiling point: {} K".format(self.boiling))
