#!/usr/bin/env python3

from stack_092 import Stack

open_paren = ['(', '{', '[']
close_paren = [')', '}', ']']
def matcher(s):
    lis = Stack()

    for sym in s:
        if sym in open_paren:
            lis.push(sym)
        elif sym in close_paren:
            pos = close_paren.index(sym)

            if not lis.is_empty() and open_paren[pos] == lis.top():
                lis.pop()
            else:
                return False
    return lis.is_empty()
