from collections import defaultdict

def summation(n):
    return n * (n + 1) // 2

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    nodes_count = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        nodes_count += 1
        visited.add(node)
        for neighbor in graph[node]:
            stack.append(neighbor)

    return nodes_count

n,m,k = [int(i) for i in input().split()]

govs = [int(i) for i in input().split()]

graph = defaultdict(list)

for _ in range(m):
    u, v = [int(i) for i in input().split()]
    
    graph[u].append(v)
    graph[v].append(u)


total_nodes_discovered = 0
max_gov_nodes = 0

edges_possible = 0
for gov in govs:
    x = dfs_iterative(graph, gov)
    max_gov_nodes = max(x, max_gov_nodes)
    total_nodes_discovered += x

max_gov_nodes
print(edges_possible - m)