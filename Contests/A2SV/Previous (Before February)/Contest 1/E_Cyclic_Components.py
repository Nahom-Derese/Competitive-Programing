from collections import defaultdict


def solve():
    n, m = [int(i) for i in input().split()]
    
    deg = [0] * n
    used = [False] * n
    g = [[] for _ in range(n)]
    
    index = 2
    for _ in range(m):
        x, y = [int(i)-1 for i in input().split()]
        index += 2
        g[x].append(y)
        g[y].append(x)
        deg[x] += 1
        deg[y] += 1
    
    ans = 0
    for i in range(n):
        if not used[i]:
            comp = []
            
            stack = [(i, used, comp, g)]
    
            while stack:
                v, used, comp, g = stack.pop()
                used[v] = True
                comp.append(v)
                
                for to in g[v]:
                    if not used[to]:
                        stack.append((to, used, comp, g))

            ok = all(deg[v] == 2 for v in comp)
            if ok:
                ans += 1
    
    print(ans)

solve()
