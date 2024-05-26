n = int(input())

dp = [0] * 3

for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    if i == 0:
        dp = [a,b,c]
        continue
    dp[0], dp[1], dp[2] = max(a + dp[1], a + dp[2]), max(b + dp[0], b + dp[2]), max(c + dp[0], c + dp[1])
    

print(max(dp))