#!/usr/bin/env python3

import sys

def main():
   list_words = sys.stdin.readlines()

   letter_17 = [word.strip() for word in list_words if len(word.strip()) == 17]
   print("Words containing 17 letters:", letter_17)

   letter_18 = [word.strip() for word in list_words if len(word.strip()) > 17]
   print("Words containing 18+ letters:", letter_18)

   shortest_word = min([word.strip() for word in list_words if all(y in word for y in 'aeiou')], key=len)
   print("Shortest word containing all vowels:", shortest_word)

   four_a = [word.strip() for word in list_words if (word.strip().lower()).count("a") == 4]
   print("Words with 4 a's:", four_a)

   more_q = [word.strip() for word in list_words if (word.strip().lower()).count("q") > 1]
   print("Words with 2+ q's:", more_q)

   cie = [word.strip() for word in list_words if "cie" in word.strip()]
   print("Words containing cie:", cie)

   anagrams = [word.strip() for word in list_words if sorted(word.strip().lower()) == sorted("angle") and word.strip().lower() != "angle"]
   print("Anagrams of angle:", anagrams)

   iary = len([word.strip() for word in list_words if (word.strip())[-4:] == "iary"])
   print("Words ending in iary:", iary)

   counts = [i.lower().count('e') for i in list_words]
   most = max(counts)
   more_e = [word.strip() for word in list_words if (word.lower()).count("e") == most]

   print("Words with most e's:", more_e)

if __name__ == "__main__":
   main()
