# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:0 for i in range(n)}


    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        size_x = self.size[parent_x]
        size_y = self.size[parent_y]

        if size_x > size_y:
            size_y, size_x = size_x, size_y

        self.parent[parent_x] = parent_y




class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted([edge + [index] for index,edge in enumerate(queries)], key=lambda x: x[2])
        ans = [False] * len(queries)

        dsu = UnionFind(n)
        
        itr = 0
        for query in queries:
            while itr < len(edgeList) and query[2] > edgeList[itr][2]:
                dsu.union(edgeList[itr][0], edgeList[itr][1])
                itr+=1
            if dsu.find(query[0]) == dsu.find(query[1]):
                
                ans[query[3]] = True
        
        return ans