import sys
from collections import *
from itertools import *
from math import *

graph = defaultdict(list)
vertice = int(input())

for i in range(vertice-1):
    v1, v2 = [int(i) for i in sys.stdin.readline().split()]
    graph[v1].append(v2)
    graph[v2].append(v1)

s = [int(i) for i in sys.stdin.readline().split()]
e = [int(i) for i in sys.stdin.readline().split()]

def bfs_by_level(start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    res = []
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        res.append(current_level)
    return res


print(bfs_by_level(1))