#!/usr/bin/env python3

def partition(lis, first, last):
    q = j = first

    while j < last:
        if lis[j] <= lis[last]:
            lis[q], lis[j] = lis[j], lis[q]
            q += 1
        j += 1

    lis[q], lis[last] = lis[last], lis[q]
    return q

def quicksort(lis, first, last):
    if last <= first:
        return

    q = partition(lis, first, last)
    quicksort(lis, first, q - 1)
    quicksort(lis, q + 1, last)
