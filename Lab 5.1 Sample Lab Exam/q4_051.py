#!/usr/bin/env python3

import sys

def main():
   nums = sorted([int(num) for num in sys.stdin])

   print("Mean: {:.1f}".format(sum(nums) / len(nums)))

   if len(nums) % 2 != 0:
      print("Median: {:.1f}".format(nums[int(len(nums) / 2)]))
   else:
      int1 = nums[int(len(nums) / 2)]
      int2 = nums[int(len(nums) / 2) - 1]
      print("Median: {:.1f}".format((int1 + int2) / 2))

if __name__ == "__main__":
   main()
