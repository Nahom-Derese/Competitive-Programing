for i in range(int(input())):
    a, b = list(map(int, input().split()))
    ans = 0
    for k in range(2, a+1):
        x = 2*k - 2
        if a%x == b:
            ans+=1
    print(ans)
            