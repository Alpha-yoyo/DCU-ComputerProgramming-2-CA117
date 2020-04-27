#!/usr/bin/env python3

import sys

def main():

   for line in sys.stdin:
      line = line.strip()

      lower = 0
      upper = 0
      digits = 0
      other = 0
      for char in line:
         if "0" <= char and char <= "9":
            digits = 1
         elif "a" <= char and char <= "z":
            lower = 1
         elif "A" <= char and char <= "Z":
            upper = 1
         else:
            other = 1
      total = lower + upper + digits + other
      print(total)


if __name__ == "__main__":
   main()
