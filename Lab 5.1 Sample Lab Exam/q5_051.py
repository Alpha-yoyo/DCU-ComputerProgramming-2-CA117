#!/usr/bin/env python3

import sys

def sec(t):
   [t1, t2] = t.split(":")
   sec = int(t1) * 60 + int(t2)
   return sec

def sort(t):
   return sec(t[-1])

def main():
   d = {}
   for line in sys.stdin:
      try:
         line = line.split()
         d[line[0]] = min(line[1:], key=sec)
      except:
         continue
   score = min(d.items(), key=sort)
   print(score[0], ":", score[1])

if __name__ == "__main__":
   main()
