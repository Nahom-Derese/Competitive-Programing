def solve():
    n = int(input())
    
    ans = [(1<<32) - 1]*n
    grid = []

    for i in range(n):
        grid.append([int(i) for i in input().split()])
        
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            ans[i] &= grid[i][j]
    
    new_grid = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            new_grid[i][j] |= ans[i]
            new_grid[i][j] |= ans[j]

    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if new_grid[i][j] != grid[i][j]:
                return []
    
    return ans

for _ in range(int(input())):
    x = solve()
    if not x:
        print("NO")
    else:
        print("YES")
        print(*x)