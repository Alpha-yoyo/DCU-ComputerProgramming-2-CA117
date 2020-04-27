#!/usr/bin/env python3

import sys

def find_width(list_strings):
   width = 0
   for string in list_strings:
      string = string.strip()
      if width < len(string):
         width = len(string)
   return(width)

def main():
   list_strings = sys.stdin.readlines()
   for string in list_strings:
      string = string.strip()

      print("{:^{}}".format(string, find_width(list_strings)))


if __name__ == "__main__":
   main()
