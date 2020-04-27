#!/usr/bin/env python3

import sys

number = int(sys.argv[1])
def main():
   multiples_of_3 = [num for num in range(3, number + 1, 3)]
   print("Multiples of 3:", multiples_of_3)

   multiples_of_3_squared = [num * num for num in range(3, number + 1, 3)]
   print("Multiples of 3 squared:", multiples_of_3_squared)

   multiples_of_4_doubled = [num * 2 for num in range(4, number + 1, 4)]
   print("Multiples of 4 doubled:", multiples_of_4_doubled)

   multiples_of_4 = [num for num in range(4, number + 1, 4)]

   multiples_of_3_or_4 = [num for num in range(3, number + 1) if num % 3 == 0 or num % 4 == 0]
   print("Multiples of 3 or 4:", multiples_of_3_or_4)

   multiples_of_3_and_4 = [num for num in range(3, number + 1) if num % 3 == 0 and num % 4 == 0]
   print("Multiples of 3 and 4:", multiples_of_3_and_4)

   multiples_of_3_replaced = [num if num % 3 != 0 else "X" for num in range(1, number + 1)]
   print("Multiples of 3 replaced:", multiples_of_3_replaced)

   prime_num = [num for num in range(2, number + 1) if all(num % num1 != 0 for num1 in range(2, num))]
   print("Primes:", prime_num)

if __name__ == "__main__":
   main()
