#!/usr/bin/env python3

def sumup(num):
    if num == 0:
        return 0
    return num + sumup(num - 1)
