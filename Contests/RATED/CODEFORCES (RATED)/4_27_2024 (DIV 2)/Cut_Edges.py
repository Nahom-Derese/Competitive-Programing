import sys
from collections import *
from itertools import *
from math import *

class DSU:
    def __init__(self, size):
        self.parent = {i:i for i in range((size+1))}
        self.size = [1] * (size+1)
        # print(self.parent)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        if self.size[parent_x] < self.size[parent_y]:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x] 
        else:
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y] 
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    n,m,k = [int(i) for i in sys.stdin.readline().split()]
    dsu = DSU(n)
    for _ in range(m):
        _,_ = sorted([int(i) for i in sys.stdin.readline().split()])

    queries = deque([])
    for _ in range(k):
        command, n1, n2 = sys.stdin.readline().split()
        n1, n2 = sorted([int(n1), int(n2)])
        queries.appendleft((command, n1, n2))
    
    ans = deque([])
    for command, n1, n2 in queries:
        if command == 'cut':
            dsu.union(n1, n2)
        else:
            if dsu.is_connected(n1, n2):
                ans.appendleft('YES')
            else:
                ans.appendleft('NO')

    print('\n'.join(ans))