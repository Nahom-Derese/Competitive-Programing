from collections import defaultdict
from collections import deque
from functools import cache
import sys



def top_sort(graph, indegree, multi_source):
    queue = deque(multi_source)
    top_sorted = []
    while queue:
        node = queue.popleft()
        top_sorted.append(node)
        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    return top_sorted


def solve():
    N, M = [int(i) for i in input().split()]

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for _ in range(M):
        x, y = [int(i) for i in input().split()]
        graph[x].append(y)
        indegree[y]+=1
        
    multi_source = [node for node in graph if not indegree[node]]


    dp = [0] * (N + 1)

    for node in top_sort(graph, indegree, multi_source):
        for child in graph[node]:
            dp[child] = max(dp[child], dp[node] + 1)
    
    return max(dp)  
    
if __name__ == "__main__":
    sys.setrecursionlimit(1 << 9)
    print(solve())