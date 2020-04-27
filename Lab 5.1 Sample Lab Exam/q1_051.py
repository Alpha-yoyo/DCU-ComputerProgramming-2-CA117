#!/usr/bin/env python3

import sys

def main():
   chars = sys.argv[1]
   lis_char = list(chars)

   i = 1
   while i < len(lis_char):
      lis_char[i - 1], lis_char[i] = lis_char[i], lis_char[i - 1]
      i += 2

   print("".join(lis_char))

if __name__ == "__main__":
   main()
