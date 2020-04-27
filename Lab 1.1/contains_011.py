#!/usr/bin/evn python3

import sys

def contains(string1, string2):
   for char in string1:
      if not(char in string2):
         return False
      else:
         string2 = string2.replace(char, "", 1)
   return True

def main():
   for line in sys.stdin:
      [string1, string2] = line.strip().lower().split()
      print(contains(string1, string2))

if __name__ == "__main__":
   main()
