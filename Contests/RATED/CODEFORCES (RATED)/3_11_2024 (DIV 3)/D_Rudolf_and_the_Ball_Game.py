from functools import cache
from collections import deque

ans = deque()

@cache
def rec(x, a, b, p):
    if b == "1":
        an = (x-a) % p
        if not an:
            return [p]
        return [an]
    
    if b == "0":
        an = (x+a) % p
        if not an:
            return [p]
        return [an]

    else:
        an1 = (x+a) % p 
        an2 = (x-a) % p
        if not an1:
            an1 = p
        if not an2:
            an2 = p 
        return [an1, an2]


for i in range(int(input())):
    n,m,x = [int(i) for i in input().split()]
    ans.append(x)

    for i in range(m):
        a,b = [i for i in input().split()]
        a = int(a)

        o = len(ans)
        for i in range(o):
            u = ans.popleft()
            ans.extend(rec(u, a, b, n))
        ans = deque(set(ans))
    
    print(len(ans))
    print(*sorted(ans))
    ans = deque()
        

            
