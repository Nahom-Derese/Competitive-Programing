import sys
from collections import *
from itertools import *
from heapq import *

# def topological_sort(graph, n):
#     indegree = defaultdict(int)
#     for neighbors in graph.values():
#         for neighbor in neighbors:
#             indegree[neighbor] += 1
    
#     queue = [node for node in range(1,n+1) if not indegree[node]]
    
#     res = []
#     while queue:
#         node = queue.pop(0)
#         res.append(node)
#         for neighbor in graph[node]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 heappush(queue, neighbor)
#     return res

def top_sort_stack(graph, n):
    indegree = defaultdict(int)
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1

    stack = [node for node in range(1, n+1) if not indegree[node]]
    heapify(stack)
    res = []
    while stack:
        node = heappop(stack)
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heappush(stack, neighbor)
    return res


n, e = [int(i) for i in sys.stdin.readline().split()]

graph = defaultdict(list)

for _ in range(e):
    e1, e2 = [int(i) for i in sys.stdin.readline().split()]
    graph[e1].append(e2)



top_sort = top_sort_stack(graph, n)

if len(top_sort) != n:
    print(-1)
else:
    print(*top_sort)