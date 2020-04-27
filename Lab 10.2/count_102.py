#!/usr/bin/env python3

def count_letters(s):
    if s == " ":
        return 0
    return sum(1 for char in s)
