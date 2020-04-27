#!/usr/bin/env python3

import sys

def main():
   number = sys.argv[1]
   number = int(number)
   i = 0
   while i < number:
      print((" " * (number - 1 - i)) + ("* " * (1 + i)).rstrip())
      i += 1

   j = 0
   while j < number - 1:
      print((" " * (1 + j) + ("* " * (number - 1 - j))).rstrip())
      j += 1

if __name__ == "__main__":
   main()
