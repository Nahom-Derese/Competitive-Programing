import sys
from collections import defaultdict
from typing import Dict, List

graph = defaultdict(list)

def neighbor_gen(v):
    for k in graph[v]:
        yield k
    
def top_sort(v, visited,stack):
        
    working_stack = [(v,neighbor_gen(v))]
        
    while working_stack:
        v, gen = working_stack.pop()
        visited[v] = True
            
        for next_neighbor in gen:
            if not visited[next_neighbor]: 
                working_stack.append((v,gen))
                working_stack.append((next_neighbor, neighbor_gen(next_neighbor)))
                break
        else:
            stack.append(v)

def TopologicalSort(n):
    visited = [False]*(n+1)
    stack = []

    for i in range(1, n+1):
        if not(visited[i]):
            top_sort(i, visited, stack)
    
    return stack

def solve():
    global graph
    graph = defaultdict(list)
    n, k = map(int, input().split())

    costs = list(map(int, input().split()))
    unlimited = list(map(int, input().split()))
    

    for i in range(n):
        graph[i+1].extend([int(i) for i in input().split()][1:])
    
    for i in range(k):
        costs[unlimited[i]-1] = 0

    order = TopologicalSort(n)
    
    for i in order:
        buying_costs = costs[i-1]
        
        mixing_costs = float("inf")
        if graph[i] != []:
            mixing_costs = sum([costs[j-1] for j in graph[i]])
        costs[i-1] = min(mixing_costs, buying_costs)
    
    print(*costs)


for _ in range(int(input())):
    solve()
