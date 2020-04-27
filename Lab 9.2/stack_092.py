#!/usr/bin/env python3

class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, num):
        self.list.append(num)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)
