# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

import sys
from collections import *
from itertools import *
from math import *

class DisjointSet:
    def __init__(self, size):
        self.parent = {i:i for i in range((size+1))}
        self.size = [1] * (size+1)
        self.min = {i:i for i in range((size+1))}
        self.max = {i:i for i in range((size+1))}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def findMinMax(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return (self.min[x], self.max[x], self.size[x])
        
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        if self.size[parent_x] < self.size[parent_y]:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x] 
            self.max[parent_y] = max(self.max[parent_y], self.max[parent_x])
            self.min[parent_y] = min(self.min[parent_y], self.min[parent_x])
        else:
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y] 
            self.max[parent_x] = max(self.max[parent_y], self.max[parent_x])
            self.min[parent_x] = min(self.min[parent_y], self.min[parent_x])
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    
n, m = [int(i) for i in sys.stdin.readline().split()]
dsu = DisjointSet(n)

for i in range(m):
    c = sys.stdin.readline().split()
    if len(c)==2:
        print(*dsu.findMinMax(int(c[1])))
    else:
        dsu.union(int(c[1]),int(c[2]))
    