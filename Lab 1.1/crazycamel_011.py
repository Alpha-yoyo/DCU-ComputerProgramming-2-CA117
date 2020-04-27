#!/usr/bin/env python3

import sys

def reverse(s):
   return(s[::-1])

def main():
   for line in sys.stdin:
      line = reverse(reverse(line.strip()).title())
      print(line)


if __name__ == "__main__":
   main()
