from itertools import accumulate

for i in range(int(input())):
    n , k = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    
    cur = 1
    for i in b:
        cur *= i
    
    if 2023 % cur == 0:
        print("YES")
        u = [2023 // cur] + ([1]*(k-1))
        print(*u)
    else:
        print("NO")