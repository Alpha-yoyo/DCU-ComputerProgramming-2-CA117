#!/usr/bin/env python3

class PQ(object):
    def __init__(self):
        self.d = {}
        self.n = 0

    def swap(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    def insert(self, v):
        self.n += 1
        self.d[self.n] = v
        self.swim(self.n)

    def swim(self, k):
        while k > 1 and self.d[k // 2] < self.d[k]:
            self.swap(k, k // 2)
            k = k // 2

    def bigger(self, i, j):
        try:
            return max([i, j], key=self.d.__getitem__)
        except KeyError:
            return i

    def sink(self, k):
        while (2 * k <= self.n):
            j = 2 * k
            j = self.bigger(j, j + 1)
            if self.d[k] >= self.d[j]:
                break
            self.swap(k, j)
            k = j

    def delMax(self):
        v = self.d[1]
        self.swap(1, self.n)
        del(self.d[self.n])
        self.n -= 1
        self.sink(1)
        return v

    def getMax(self):
        return self.d[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.n
