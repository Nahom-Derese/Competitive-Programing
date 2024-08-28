from collections import defaultdict, deque


n, m = [int(i) for i in input().split()]

graph = defaultdict(list)

def bfs(u, v):
    queue = deque([(u, 0)])
    
    ans = set()
    visited = set()
    while queue:
        b, c = queue.popleft()

        visited.add((b,c))

        if b == v:
            ans.add(c)

        for neig in graph[b]:
            if neig in visited:
                continue
            if neig[1] == c or c == 0:
                queue.append(neig)

    return len(ans)


for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    graph[a].append((b, c))
    graph[b].append((a, c))
    
for _ in range(int(input())):
    u, v = [int(i) for i in input().split()]
    
    print(bfs(u, v))

