#!/usr/bin/env python3

import sys


def check(left, right):
   if len(left) != len(right):
      return False
   for c in left:
      if not(c in right):
         return False
      else:
         right = right.replace(c, " ", 1)
   return True


def main():
   for line in sys.stdin:
      [string1, string2] = line.strip().split()
      print(check(string1, string2))


if __name__ == "__main__":
   main()
