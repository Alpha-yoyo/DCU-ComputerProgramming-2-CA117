#!/usr/bin/env python3

import sys


def main():
   for line in sys.stdin:
      line = line.split("@")
      name = line[0].split(".")
      first_name = name[0].title()
      i = 0
      while i < len(name[1]) and (name[1][i] < "0" or "9" < name[1][i]):
         i += 1
      if i < len(name[1]):
         surname = name[1][0:i].title()
      print(first_name + " " + surname)

if __name__ == "__main__":
   main()
