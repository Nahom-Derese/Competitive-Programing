from sys import stdin

input = stdin.readline

from collections import deque

n, q = map(int, input().split())

nums = deque([int(i) for i in input().split()])
max_index = nums.index(max(nums))

def doublePopLeft(c):
    u = nums.copy()
    for j in range(c):
        if u[0] > u[1]:
            y = u.popleft()
            x = u.popleft()
            u.append(x)
            u.appendleft(y)
        else:
            x = u.popleft()
            u.append(x)
        
    return list(u)

for i in range(q):
    query = int(input())
    shift = min(query-1, max_index)
    y = doublePopLeft(shift)

    if query >= n:
        formula = (query - (max_index+1)) % (n-1) 
        print(y[0], y[1:][formula])
    else:
        print(y[0], y[1])