#!/usr/bin/env python3

import sys

def main():
   for line in sys.stdin:
      line = line.strip().split()
      print(line[0].lower() in line[1].lower())


if __name__ == "__main__":
   main()
