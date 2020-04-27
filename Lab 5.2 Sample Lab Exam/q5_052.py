#!/usr/bin/env python3

import sys

def total_mark(lis):
   return sum(lis)

def sort(pair):
   return pair[-1]
def main():
   d = {}
   ignore = []
   for line in sys.stdin:
      name, mark = line.strip().split(":")
      mark = mark.split(",")
      try:
         int_mark = list(map(int, mark))
         d[name] = total_mark(int_mark)
      except:
         ignore.append(name)

   t_mark = sorted(d.items(), key=sort, reverse=True)
   for score in t_mark:
      print(score[0], ":", score[1])
   print("Skipped:")
   for name in ignore:
      print(name)

if __name__ == "__main__":
   main()
