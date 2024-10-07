def solve():
    n, k = [int(i) for i in input().split()]
    s = input()
    
    ans = False
    
    l = 0
    r = n - 1
    
    while l + 1 < r and s[l] == s[r]:
        l += 1
        r -= 1

    return l >= k

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")