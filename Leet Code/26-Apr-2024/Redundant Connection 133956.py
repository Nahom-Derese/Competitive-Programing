# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class DisjointSet:
    def __init__(self, size):
        self.parent = {i:i for i in range(size+1)}
        self.size = [1] * (size+1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        x = self.find(self.parent[x])
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


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DisjointSet(len(edges))
        
        for x,y in edges:
            if not dsu.union(x,y):
                return [x,y]