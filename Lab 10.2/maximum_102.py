#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    l = sorted(l, reverse=True)
    return l[0]
