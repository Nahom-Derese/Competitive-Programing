def solve():
    n = int(input())
    ans = 0
    
    while n % 5 == 0 and n>1:
        n //= 5
        ans += 3


    while n % 3 == 0 and n>1:
        n //= 3
        ans += 2
    
    while n & 1 == 0 and n>1:
        n >>= 1
        ans += 1

    if n == 1:
        print(ans)
    else:
        print(-1)


for _ in range(int(input())):
    solve()
