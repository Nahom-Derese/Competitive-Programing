import sys
from collections import *
from itertools import *
from math import *

graph = defaultdict(list)
colors = []


def bfs_by_level(start):
    global colors
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    res = []
    ans = 0
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node, color = queue.popleft()
            
            ans+=color != colors[node-1]
            
            current_level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if color != colors[node-1]:
                        queue.append((neighbor, colors[node-1]))
                    else:
                        queue.append((neighbor, color))
        res.append(current_level)
    return ans



def solve_problem():
    global colors
    vertices = int(sys.stdin.readline().strip())
    edges = [int(i) for i in sys.stdin.readline().split()]
    colors = [int(i) for i in sys.stdin.readline().split()]
    
    for i in range(1, vertices):
        graph[i+1].append(edges[i-1])
        graph[edges[i-1]].append(i+1)

    print(bfs_by_level(1))
    

if __name__ == '__main__':
    solve_problem()