#!/usr/bin/env python3

import sys

def main():
   for line in sys.stdin:
      line = line.strip()
      word = [chars.lower() for chars in line if chars.lower() in "aeiou"]

      if word == list("aeiou"):
         print(line)

if __name__ == "__main__":
   main()
