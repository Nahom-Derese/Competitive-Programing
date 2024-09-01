from collections import defaultdict, deque, Counter



def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    traversal = []

    while stack:
        node = stack.pop()
        traversal.append(node)
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            stack.append(neighbor)
    
    return traversal


q = int(input())


graph = defaultdict(deque)
starter = 0

itr = 0

freq = Counter()
remove_q = Counter()

for _ in range(q):
    command = input().split()
    
    if len(command) == 3:
        # insert X after Y
        _, x, y = command
        
        freq[x]+=1
        if itr == 0:
            starter = y
            graph[(y, 0)].appendleft((x, freq[x]))
        else:
            graph[(y, remove_q[y]+1)].appendleft((x, freq[x]))
        itr+=1
    else:
        # remove x
        _, x = command
        if freq[x]:
            remove_q[x]+=1
            freq[x]-=1
        
    
ans = []
for num in dfs_iterative(graph, (starter, 0)):
    
    if num[1] <= remove_q[num[0]]:
        continue
    ans.append(num[0])

# print(dict(graph))
print(" ".join(ans))