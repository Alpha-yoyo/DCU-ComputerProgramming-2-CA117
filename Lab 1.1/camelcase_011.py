#!/usr/bin/env python3

import sys

def main():
   for line in sys.stdin:
      line = line.strip().title()
      print(line)


if __name__ == "__main__":
   main()
