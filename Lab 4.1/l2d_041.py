#!/usr/bin/env python3

import sys

def l2d(file):
   keys = file.readline().strip().split()
   values = file.readline().strip().split()
   return(dict(zip(keys, values)))

def main():
   d = l2d(sys.stdin)
   for (k, v) in sorted(d.items()):
      print("{} : {}".format(k, v))

if __name__ == "__main__":
   main()
