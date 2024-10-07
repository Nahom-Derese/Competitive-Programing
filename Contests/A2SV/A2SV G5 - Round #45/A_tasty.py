n, m = [int(i) for i in input().split()]

x, r = divmod(n, m)

ans = [x]*m

for i in range(r):
    ans[m-1-i] += 1

print(*ans)