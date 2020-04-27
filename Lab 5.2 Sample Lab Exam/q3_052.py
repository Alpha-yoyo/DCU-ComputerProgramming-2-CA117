#!/usr/bin/env python3

def build_dictionary(filename):
   d = {}
   with open(filename) as file:
      for line in file:
         [k, v] = line.strip().split()
         d[k] = int(v)
   return d

def extract_range(d, low, high):
   nd = {}
   for k, v in d.items():
      if low <= v and v <= high:
         nd[k] = v
   return nd
