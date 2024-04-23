import sys
from collections import *
from itertools import *
from math import *

def topological_sort(graph, n):
    indegree = defaultdict(int)
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    queue = deque([node for node in range(1, n+1) if indegree[node] == 0])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return res


for i in range(int(input())):
    n, m = map(int, input().split())

    graph = defaultdict(list)
    undirected = []
    directed = []
    
    for i in range(m):
        d, v1, v2 = map(int, input().split())
        if not d:
            undirected.append((v1, v2))
        else:
            directed.append((v1, v2))
            graph[v1].append(v2)

    top_sort = topological_sort(graph, n)
    
    if len(top_sort) != n:
        print("NO")
    else:
        print("YES")
        indices = defaultdict(int)
        for i in range(len(top_sort)):
            indices[top_sort[i]] = i
        for query in undirected:
            if indices[query[0]] > indices[query[1]]:
                print(query[1], query[0])
            else:
                print(*query)
        for query in directed:
            print(*query)
