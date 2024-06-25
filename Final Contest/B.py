class UnionFind:
    def __init__(self, matrix) -> None:
        self.parent = {}
        self.size = {}

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.parent[(i,j)] = (i,j)
                self.size[(i,j)] = matrix[i][j]

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
    n = int(input())
    
    matrix = [list(input()) for i in range(n)]

    DSU = UnionFind(matrix)

    for j in range(n):
        for i in range(n):
            DSU.union((j, i) , (n-1-i, j))
    
    ans = 0
    for j in range(n):
        for i in range(n):    
            x = DSU.find((i,j))
            ans+= abs(ord(matrix[i][j]) - ord(matrix[x[0]][x[1]]))

    return ans

for _ in range(int(input())):
    print(solve())
