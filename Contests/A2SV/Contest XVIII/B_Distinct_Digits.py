import sys
from collections import deque

def solve():
    n = int(input())

    ans = deque()
    for i in range(9, 0, -1):
        if n >= i:
            ans.appendleft(i)
            n -= i
        if n == 0:
            break
    print(''.join(map(str, ans)))

for _ in range(int(input())):
    solve()
