#!/usr/bin/env python3

import sys
import math

def main():
   rank_name = {
      0: "nothing",
      1: "one pair",
      2: "two pairs",
      3: "three of a kind",
      4: "a straight",
      5: "a flush",
      6: "a full house",
      7: "four of a kind",
      8: "a straight flush",
      9: "a royal flush"
   }
   list_rank = []
   line = sys.stdin.readlines()
   for hands in line:
      hands = hands.strip().split(",")
      list_rank.append(int(hands[-1]))

   total_rank = len(list_rank)
   count = []
   percentage = []
   for rank_num in range(10):
      count.append(list_rank.count(rank_num))
      percentage.append((count[rank_num] / total_rank) * 100)

   for rank_num in range(10):
      print("The probability of {:s} is {:.4f}%".format(rank_name[rank_num], percentage[rank_num]))

if __name__ == "__main__":
   main()
