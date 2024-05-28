# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/


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

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def reset(self, x: int) -> None:
        self.parent[x] = x
        self.size[x] = 0

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = collections.defaultdict(list)
        for x, y, t in meetings: g[t].append((x, y))


        DSU = UnionFind(n)
        DSU.union(0, firstPerson)
        for _, v in sorted(g.items()):
            for x, y in v:
                DSU.union(x, y)
            for x, y in v:
                if not DSU.is_connected(x, 0): 
                    DSU.reset(x)
                    DSU.reset(y)
            
    
        ans = []

        for i in range(n):
            if DSU.is_connected(i, 0):
                ans.append(i)

        return ans