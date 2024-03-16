for i in range(int(input())):
    n, m, k = [int(i) for i in input().split()]

    pocket1 = sorted([int(i) for i in input().split()])
    pocket2 = sorted([int(i) for i in input().split()])

    ans = 0
    
    for i in range(n):
        for j in range(m):
            if pocket1[i] + pocket2[j] <= k:
                ans += 1
            else:
                break
    
    print(ans)
        
    