import sys
from collections import *
from itertools import *
from math import *

class DSU:
    def __init__(self, size):
        self.parent = {i:i for i in range((size+1))}
        self.exprience = {i:0 for i in range((size+1))}
        self.extra = {i:0 for i in range((size+1))}
        self.size = [1] * (size+1)
        self.n = size+1

    def get(self, x):
        if x == self.parent[x]:
            return self.exprience[x]
        return self.exprience[x] - self.extra[x] + self.get(self.parent[x])
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 
    
    def add(self, x, points):
        self.exprience[self.find(x)] += points

    def union(self, x, y):
        if (x < 0 or x>=self.n or y < 0 or y>=self.n):
            return False
        parent_x = self.find(x)
        parent_y = self.find(y)


        if parent_x == parent_y:
            return False

        if self.size[parent_x] < self.size[parent_y]:
            parent_x, parent_y = parent_y, parent_x

        self.parent[parent_y] = parent_x
        self.size[parent_x] += self.size[parent_y] 
        self.extra[parent_y] = self.exprience[parent_x] 
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


def solve_problem(command, dsu):
    if len(command) == 2:
        x = int(command[1])
        return dsu.get(x)
    elif command[0] == "add":
        x, points = [int(i) for i in command[1:]]
        dsu.add(x, points)
    else:
        x, y = [int(i) for i in command[1:]]
        dsu.union(x, y)

if __name__ == '__main__':
    n, m = map(int, input().split())
    dsu = DSU(n)
    for _ in range(m):
        c = sys.stdin.readline().strip().split()
        ans = solve_problem(c, dsu)
        if ans != None:
            print(ans)