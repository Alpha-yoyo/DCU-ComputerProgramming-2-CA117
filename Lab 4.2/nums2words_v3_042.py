#!/usr/bin/env python3

import sys

def main():
   with open(sys.argv[1]) as file:
      file = file.read().split()
      num = file[::2]
      lan = file[1::2]
      trans = dict(zip(num, lan))

   convert = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
   number = [line.strip().split() for line in sys.stdin]

   for l in number:
      a = []
      for num1 in l:
         a.append(trans[convert[num1]])
      print(" ".join(a))

if __name__ == "__main__":
   main()
