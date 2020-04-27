#!/usr/bin/env python3

import sys

def main():
   for line in sys.stdin:
      line = line.strip()
      word = [char.lower() for char in line if char.lower() in "evil"]
      if word == list("evil"):
         print(line)

if __name__ == "__main__":
   main()
