#!/usr/bin/env python3

import sys

def main():
   convert = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
   num = [line.strip().split() for line in sys.stdin]

   for l in num:
      a = []
      for num1 in l:
         a.append(convert[int(num1)])
      print(" ".join(a))

if __name__ == "__main__":
   main()
