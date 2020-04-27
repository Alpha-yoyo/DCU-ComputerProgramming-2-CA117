#!/usr/bin/env python3

import sys
import math

def main():
   number = sys.argv[1]
   print("{:.{}f}".format(math.pi, number))

if __name__ == "__main__":
   main()
