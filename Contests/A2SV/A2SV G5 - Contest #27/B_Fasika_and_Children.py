from collections import deque

n, m = [int(i) for i in input().split()]
candy_wants = deque([(int(i), index+1) for index, i in enumerate(input().split())])

while candy_wants:
    x = candy_wants.popleft()
    y = x[0] - m
    if y > 0:
        candy_wants.append((y, x[1]))
    if not candy_wants:
        print(x[1])

