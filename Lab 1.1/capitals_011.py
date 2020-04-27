#!/usr/bin/env python3

import sys

def reverse(s):
   return(s[::-1])

def main():
   for line in sys.stdin:
      line = line.strip()
      if len(line) > 1:
         capital1 = line[0].upper()
         capital2 = line[-1].upper()
         total = capital1[0] + line[1:-1] + capital2
         print(total)

if __name__ == "__main__":
   main()
