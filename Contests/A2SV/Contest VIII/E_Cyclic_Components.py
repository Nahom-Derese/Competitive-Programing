import sys
from collections import *
from itertools import *
from math import *

graph = defaultdict(list)
v, e = [int(i) for i in sys.stdin.readline().split()]

def dfs_cycle():
    visited = set()
    cycle_count = 0
    for i in graph.keys():
        if i not in visited:
            stack = [(i, -1)]
            visited.add(i)
            while stack:
                node, parent = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, node))
                    elif neighbor != parent:
                        cycle_count+=1
    return cycle_count


for _ in range(e):
    v1, v2 = [int(i) for i in sys.stdin.readline().split()]

    graph[v1].append(v2)
    graph[v2].append(v1)


print(dfs_cycle())




