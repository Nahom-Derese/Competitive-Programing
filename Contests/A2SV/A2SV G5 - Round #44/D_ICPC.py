from collections import defaultdict

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix

def solve():
    n = int(input())
    
    ui = list(map(int, input().split()))
    si = list(map(int, input().split()))
    
    graph = defaultdict(list)
    
    for u, s in zip(ui, si):
        graph[u].append(s)
    
    for uni in graph:
        graph[uni].sort(reverse=True)
        graph[uni] = prefix_sum(graph[uni])
    
    ans = [0] * n
    
    for uni in graph:
        length_uni = len(graph[uni]) - 1
        for i in range(1, length_uni + 1):
            full_teams = length_uni // i
            ans[i - 1] += graph[uni][full_teams * i]
    
    print(*ans)

for _ in range(int(input())):
    solve()
