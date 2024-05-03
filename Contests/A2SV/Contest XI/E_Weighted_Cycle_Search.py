import sys
from collections import *
from itertools import *
from math import *

def bfs(graph, start, target):
    prev = {start: -1}
    queue = deque([start])
    while queue:
        
        node = queue.popleft()
        
        if node == target:
            break
        
        for neighbor in graph[node]:
            if neighbor not in prev:
                prev[neighbor] = node
                queue.append(neighbor)
    if target not in prev:
        return -1
    
    path = []
    itr = target
    while itr != -1:
        path.append(itr)
        itr = prev[itr]
    
    return path[::-1]
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



if __name__ == '__main__':
    for i in range(int(input())):
        graph = defaultdict(list)
        v, e = [int(i) for i in sys.stdin.readline().split()]
    
        dsu = DSU(v)
        edges = []
        for _ in range(e):
            a, b, c = [int(i) for i in sys.stdin.readline().split()]
            
            edges.append((c,a,b))
        edges.sort(reverse=True)

        _min = float("inf")
        ans = ()
        for c, a, b in edges:
            if not dsu.is_connected(a,b):
                dsu.union(a,b)
                graph[a].append(b)
                graph[b].append(a)
            else:
                _min = c
                ans = (a,b)
        ui = bfs(graph, *ans)
        print(_min, len(ui))
        print(*ui)