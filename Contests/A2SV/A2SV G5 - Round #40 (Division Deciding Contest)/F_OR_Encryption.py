def solve():
    n = int(input())
    
    ans = [(1<<32) - 1]*n
    grid = []

    for i in range(n):
        grid.append([int(i) for i in input().split()])
        
    
    for i in range(n):
        for j in range(i+1, n):
            ans[i] &= grid[i][j]
    
    new_grid = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            new_grid[i][j] |= ans[i]
            new_grid[i][j] |= ans[j]

    for i in range(n):
        for j in range(i+1, n):
            print(grid[i][j], end=" ")
            # if new_grid[i][j] != grid[i][j]:
            #     return []
        print()
    print(ans)
    return ans

for _ in range(int(input())):
    x = solve()
    # if not x:
    #     print("NO")
    # else:
    #     print("YES")
    #     print(*x)