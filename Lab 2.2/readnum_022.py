#!/usr/bin/env python3

import sys

def main():

   for line in sys.stdin:
      line = line.strip()
      try:
         number = int(line)
         print("Thank you for {:d}".format(number))
         break
      except:
         print("{:s} is not a number".format(line))

if __name__ == "__main__":
   main()
