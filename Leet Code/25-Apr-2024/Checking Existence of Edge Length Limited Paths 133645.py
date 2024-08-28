# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind():
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = defaultdict(int)
    
    def find(self, x):
        if self.parent[x]==x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x,y):
        xx=self.find(self.parent[x])
        yy=self.find(self.parent[y])
        if xx!=yy :
            if self.rank[yy] < self.rank[xx]:
                self.parent[yy] = xx
            elif self.rank[xx] < self.rank[yy]:
                self.parent[xx] = yy
            else:
                self.rank[xx]+=1
                self.parent[yy]=xx

    def connected(self, x, y):
        return self.find(x) == self.find(y)


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
            if dsu.connected(query[0], query[1]):
                
                ans[query[3]] = True
        
        return ans