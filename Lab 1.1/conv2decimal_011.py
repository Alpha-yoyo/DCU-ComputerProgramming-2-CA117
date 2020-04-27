#!/usr/bin/env python3

import sys

def reverse(s):
   return(s[::-1])

def main():
   for line in sys.stdin:
      [number, base] = line.strip().split()
      base = int(base)
      print(int(number, base))


if __name__ == "__main__":
   main()
