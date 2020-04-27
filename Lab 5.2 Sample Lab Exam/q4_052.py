#!/usr/bin/env python3

import sys

def cal(filename):
   d = {}
   with open(filename) as file:
      for line in file:
         k, v = line.strip().rsplit(maxsplit=1)
         d[k] = int(v)
   return d

def sort(t):
   return t[-1]

def main():
   d = cal(sys.argv[1])

   d1 = {}
   for line in sys.stdin:
      line = line.strip().split(",")
      name, foods = line[0], line[1:]
      d1[name] = 0

      for food in foods:
         if food in d:
            d1[name] += d[food]
         else:
            d1[name] += 100

   max_name = len(max(d1.keys(), key=len))
   max_value = len(str(max(d1.values())))
   for k, v in sorted(d1.items(), key=sort):
      print("{:>{:d}s} : {:{:d}d}".format(k, max_name, v, max_value))

if __name__ == "__main__":
   main()
