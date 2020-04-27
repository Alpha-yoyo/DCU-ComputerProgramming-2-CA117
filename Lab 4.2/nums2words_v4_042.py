#!/usr/bin/env python3

import sys

def main():
   num = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
   word = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

   num_word = [line.strip().split() for line in sys.stdin]
   for l in num_word:
      a = []
      for num1 in l:
         if num1 == "100":
            a.append("one hundred")
         elif 0 <= int(num1) <= 19:
            a.append(num[num1])
         elif 20 <= int(num1) <= 99:
            int1, int2 = divmod(int(num1), 10)
            if num1[1] == "0":
               a.append(word[int1 - 2])
            else:
               a.append(word[int1 - 2] + "-" + num[str(int2)])
      print(" ".join(a))

if __name__ == "__main__":
   main()
