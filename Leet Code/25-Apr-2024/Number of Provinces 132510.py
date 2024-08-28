# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.rank = [0] * size

        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

		
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        
        if xx != yy:    
            if self.parent[xx] < self.parent[yy]:
                self.parent[xx] = self.parent[yy]
            if self.parent[yy] > self.parent[xx]:
                self.parent[yy] = self.parent[xx]
            else:
                self.rank[xx]+=1
                self.parent[xx] = self.parent[yy]
        print(self.parent)


    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(int)
        ans = len(isConnected)
        dsu = UnionFind(ans)
        for r in range(len(isConnected)):
            for c in range(0, r+1):
                if isConnected[r][c] and not dsu.connected(r,c):
                    ans-=1
                    dsu.union(r,c)
        return ans