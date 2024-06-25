def solve():
    n, k, x = map(int, input().split())
    minimum = 1 + int(x == 1)

    if minimum > n or (n % 2 and k == 2 and x == 1) or k == 1:
        print("NO")
        return
    
    print("YES")
    if minimum == 1:
        print(n)
        print(*([1]*n))
    else:
        if n % 2:
            ans = [2] * (n // 2 - 1)
            ans.append(3)
        else:
            ans = [2] * (n // 2)
        print(len(ans))
        print(*ans)
for _ in range(int(input())):
    solve()
