# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class DSU:
    def __init__(self, size):
        self.parent = {i:i for i in range((size+1))}
        self.size = [1] * (size+1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # roads.sort(key=lambda x: x[2])
        # dsu = DSU(n)

        # for x,y,d in roads:
        #     dsu.union(x,y)

        graph = defaultdict(list)
        visited = set()

        for x,y,d in roads:
            graph[y].append((x,d))
            graph[x].append((y,d))

        stack = [(1, float("inf"))]
        ans = float("inf")
        while stack:
            x = stack.pop()
            ans = min(x[1], ans)
            visited.add(x[0])

            for i in graph[x[0]]:
                if i[0] in visited:
                    continue
                stack.append(i)

        return ans