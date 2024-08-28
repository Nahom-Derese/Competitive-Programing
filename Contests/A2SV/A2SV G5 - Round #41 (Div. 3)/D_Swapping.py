class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = {i:i for i in range(1, n+1)}
        self.size = {i:1 for i in range(1, n+1)}

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
    n, x, m = [int(i) for i in input().split()]
    
    DSU = UnionFind(n)

    stack = []
    for _ in range(m):
        l, r = [int(i) for i in input().split()]
        if  l <= x <= r:
            DSU.union
        

for _ in range(int(input())):
    solve()
