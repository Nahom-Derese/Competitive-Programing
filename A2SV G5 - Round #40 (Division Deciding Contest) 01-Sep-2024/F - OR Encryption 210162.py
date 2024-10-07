# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

def solve():
    n = int(input())
    
    ans = [(1<<30) - 1]*n
    grid = []

    for i in range(n):
        grid.append([int(i) for i in input().split()])
        
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            ans[i] &= grid[i][j]
    
    for i in range(n):
        for j in range(i+1, n):
            if grid[i][j] != ans[i] | ans[j]:
                return []

    return ans

for _ in range(int(input())):
    x = solve()
    if not x:
        print("NO")
    else:
        print("YES")
        print(*x)
