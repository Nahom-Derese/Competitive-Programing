# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n+1)}
        self.size = {i:1 for i in range(n+1)}

    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return 0
        
        size_x = self.size[parent_x]
        size_y = self.size[parent_y]

        if size_x > size_y:
            parent_x, parent_y = parent_y, parent_x
            size_x, size_y = size_y, size_x
        
        self.parent[parent_x] = parent_y
        self.size[parent_y] += size_x

        return size_y * size_x
        

class Solution:
    def summation(self, n:int):
        return int((n + 1) * (n/2))

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        DSU = UnionFind(n)
        all_connections = self.summation(n-1)
        
        for x, y in edges:
            all_connections -= DSU.union(x,y)
        
        return all_connections