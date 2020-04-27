#!/usr/bin/env python3

def selectionsort(lis):
    i = 0
    while i < len(lis):
        p = i
        j = i + 1
        while j < len(lis):
            if lis[j] < lis[p]:
                p = j
            j += 1

        lis[p], lis[i] = lis[i], lis[p]

        i += 1
