import sys
from collections import *
from itertools import *
from math import *

class UnionFind:
    def __init__(self, size):
        self.root = {i : i for i in range(size)}
        self.ans = {i : [i] for i in range(size)}
        self.size = [1] * size
    
    def findAns(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return [i+1 for i in self.ans[x]]
    
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.ans[rootX].extend(self.ans[rootY])
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.ans[rootY].extend(self.ans[rootX])

n = int(input())
dsu = UnionFind(n)
for _ in range(n-1):
    n1, n2 = [int(i) for i in sys.stdin.readline().split()]
    dsu.union(n1-1, n2-1)

print(*dsu.findAns(0))