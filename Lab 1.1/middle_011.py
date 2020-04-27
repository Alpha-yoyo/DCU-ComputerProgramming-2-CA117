#!/usr/bin/env python3

import sys

def middle(s):
   if len(s) % 2 == 1:
      return(s[int(len(s) / 2)])
   else:
      return("No middle character!")
def main():
   for line in sys.stdin:
      line = line.strip()
      center = (middle(line))
      print(center)

if __name__ == "__main__":
   main()
