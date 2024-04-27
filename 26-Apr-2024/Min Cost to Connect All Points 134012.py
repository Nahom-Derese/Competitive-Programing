# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class DisjointSet:
    def __init__(self, points):
        self.parent = {i:i for i in points}
        self.size = {i:1 for i in points}

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(i) for i in points]

        dsu = DisjointSet(points)

        def manhattan(pair):
            x, y = pair
            xi, yi = x 
            xj, yj = y
            return (x, y, abs(xi - xj) + abs(yi - yj))

        pairs = []
        for index, pt2 in enumerate(points):
            for i in range(index+1, len(points)):
                pt1 = points[i]
                pairs.append((pt2, pt1))
        
        pairs = [manhattan(i) for i in pairs]
        pairs.sort(key=lambda x:x[2])
        
        not_connected = len(points)
        itr = ans = 0
        while not_connected and itr < len(pairs):
            x, y, distance = pairs[itr]
            if dsu.union(x,y):
                ans+=distance
                not_connected-=1
            itr+=1

        return ans