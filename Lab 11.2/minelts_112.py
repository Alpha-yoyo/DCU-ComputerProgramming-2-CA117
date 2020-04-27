#!/usr/bin/env python3

from priority_queue_112 import PQ
import sys

num = int(sys.argv[1])

pq = PQ()
for line in sys.stdin:
    pq.insert(int(line.strip()))

for i in range(len(pq.d) - num):
    pq.delMax()

for j in range(num):
    print(pq.delMax())
