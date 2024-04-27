import sys

def bool_to_string(b):
    return 'YES' if b else 'NO'

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)



n, m = [int(i) for i in sys.stdin.readline().split()]
dsu = DSU(n+1)

for i in range(m):
    c = sys.stdin.readline().split()
    if c[0]=='get':
        print(bool_to_string(dsu.is_connected(int(c[1]),int(c[2]))))
        
    else:
        dsu.union(int(c[1]),int(c[2]))