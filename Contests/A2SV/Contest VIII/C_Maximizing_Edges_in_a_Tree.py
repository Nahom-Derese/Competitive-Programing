import sys
from collections import *
from itertools import *
from math import *
from collections import deque

graph = defaultdict(list)


def is_bipartite_iterative():
    red = set()
    black = set()
    stack = deque()
    stack.append((1, 1))
    while stack:
        node, color = stack.pop()
        if color > 0: red.add(node)
        else: black.add(node)
        for neighbor in graph[node]:
            same_color = (color > 0 and neighbor in red) or (color < 0 and neighbor in black)
            if same_color:
                return False
            notFound = not(neighbor in red or neighbor in black)
            if notFound:
                stack.append((neighbor, -1*color))
    return len(red) * len(black)


n = int(input())
for i in range(n-1):
    n_1, n_2 = [int(i) for i in sys.stdin.readline().split()]
    graph[n_1].append(n_2)
    graph[n_2].append(n_1)

possible_edges = is_bipartite_iterative()
edges = n-1

print(possible_edges - edges)