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

        

# test = int(input())
# for _ in range(test):
#    ln = int(input())
#    res = []
#    mat = []
#    for i in range(ln):
#       r = [int(i) for i in input().split()]
#       mat.append(r)
#       cur = pow(2,30)-1
#       for j in range(ln):
#          # print(i,j,r[i],r,cur)
#          if i!=j:
#             cur = cur & r[j]
#       res.append(cur)
#    # print(res)
#    flag = True
#    for i in range(ln):
#       for j in range(i+1,ln):
#          if mat[i][j] != res[i]|res[j]:
#             flag = False
#    if flag:
#       print("YES")
#       print(*res)
#    else:
#       print("NO")