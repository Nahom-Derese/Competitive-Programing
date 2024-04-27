# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class DSU:
    def __init__(self, string):
        self.parent = {i:i for i in string}
        self.rank = {i:0 for i in string}
        self.min = {i:i for i in string}


    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def findMin(self, x):
        if x not in self.parent:
            return x
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.min[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.min[root_y] = min(self.min[root_y], self.min[root_x])
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.min[root_x] = min(self.min[root_y], self.min[root_x])
        else:
            self.parent[root_x] = root_y
            self.min[root_y] = min(self.min[root_y], self.min[root_x])
            self.rank[root_y] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU(s1+s2)
        
        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])

        return "".join(map(lambda x: dsu.findMin(x), baseStr))