import sys
from collections import *
from itertools import *
from math import *


graph = defaultdict(list)
path = []

v, e = [int(i) for i in sys.stdin.readline().split()]


for _ in range(e):
    n_1, n_2 = [int(i) for i in sys.stdin.readline().split()]    
    graph[n_1].append(n_2)
    graph[n_2].append(n_1)

middles = 0
edges = 0
center = 0
for i in graph:
    edges += len(graph[i]) == 1
    center += len(graph[i]) == v-1
    middles += len(graph[i]) == 2

if middles == len(graph):
    print("ring topology")
elif middles == len(graph)-2 and edges == 2:
    print("bus topology")
elif edges == v-1 and center == 1:
    print("star topology")
else:
    print("unknown topology")