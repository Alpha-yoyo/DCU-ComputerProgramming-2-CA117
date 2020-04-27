#!/usr/bin/env python3

import sys

def main():
   with open(sys.argv[1]) as file:
      file = file.read().split()

   list_lines = sys.stdin.readlines()
   for line in list_lines:
      line = line.strip()
      for banned in file:
         line = line.replace(banned, "@" * len(banned))
      print(line)


if __name__ == "__main__":
   main()
