#!/usr/bin/env python3

import sys

def transform(s):
   for cap in s:
      if cap.isupper():
         return cap
      else:
         return "0"

def main():
   for line in sys.stdin:
      line = line.strip()
      word = [transform(char) for char in line]
      word = "".join(word)
      cap = word.split("0")
      print(max(cap, key=len))

if __name__ == "__main__":
   main()
