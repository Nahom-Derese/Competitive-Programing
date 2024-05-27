# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = {i:i for i in range(n+1)}
        self.size = {i:1 for i in range(n+1)}

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.size[px] > self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]



def solve():
    n, m = [int(i) for i in input().split()]
    g = defaultdict(list)
    
    edges = []
    for _ in range(m):
        x, y = [int(i)-1 for i in input().split()]
        edges.append((x,y))
        g[x].append(y)
        g[y].append(x)

    DSU = UnionFind(n)
    ans = 0
    for x,y in edges:
        if DSU.find(x) == DSU.find(y):
            ans+=1
        if len(g[x]) == 2 and len(g[y]) == 2:
            DSU.union(x, y)
    return ans

print(solve())