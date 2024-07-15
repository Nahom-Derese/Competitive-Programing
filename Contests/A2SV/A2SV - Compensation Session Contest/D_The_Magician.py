class UnionFind:
    def __init__(self) -> None:
        self.parent = {i:i for i in range(26)}
        self.size = {i:1 for i in range(26)}

    def find(self, x: str) -> str:
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

    def is_connected(self, x:int, y:int):
        px, py = self.find(x), self.find(y)
        return px == py



def solve():
    n,k = [int(i) for i in input().split()]
    s = input()
    t = input()
    
    DSU = UnionFind()

    for i in range(k):
        for j in range(k, n-i, k):
            o = ord(s[i]) - ord("a")
            p = ord(s[i + j]) - ord("a")
            DSU.union(o, p)
            if i + j + 1 < n:
                q = ord(s[i + j + 1]) - ord("a")
                DSU.union(o, q)
    
    for i in range(n):
        o = ord(s[i]) - ord("a")
        p = ord(t[i]) - ord("a")
        if not DSU.is_connected(o, p):
            return False
    
    return True

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")
