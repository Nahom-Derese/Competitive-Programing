import sys
from collections import *
from itertools import *
from math import *
from collections import deque

graph = defaultdict(list)

def dfs(start):
    visited = set()
    stack = [start]
    visited.add(start)
    max_dist = 0
    while stack:
        node = stack.pop()
        
        visited.add(node[0])
        
        max_dist = max(node[1], max_dist)
        
        for neighbor in graph[node[0]]:
            if neighbor[0] not in visited:
                stack.append((neighbor[0], node[1]+neighbor[1]))
    
    return max_dist


def solve_problem():
    vertices = int(sys.stdin.readline().strip())
    
    for _ in range(vertices-1):
        v1, v2, d = [int(i) for i in sys.stdin.readline().split()]
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))
    
    return dfs((0,0))
    
    
        

if __name__ == '__main__':
    print(solve_problem())