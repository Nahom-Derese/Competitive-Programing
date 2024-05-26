N, W = [int(i) for i in input().split()]
items = []


for _ in range(N):
    w, v = [int(x) for x in input().split()]
    items.append((w,v))

dp = [[0] * (W+1) for i in range(2)]


for r in range(1, N+1):
    for c in range(1, W+1):
        w, v = items[r-1]
        if c-w > -1:
            dp[1][c] = max(dp[0][c-w] + v, dp[0][c])
        else:
            dp[1][c] = dp[0][c]
    dp[0] = dp[1].copy()


print(dp[1][W])