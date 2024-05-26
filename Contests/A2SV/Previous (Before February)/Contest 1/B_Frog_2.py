n, k = [int(x) for x in input().split()]
stones = [int(x) for x in input().split()]

def solve():
    if n == 1:
        print(0)
        return

    if n < k+1:
        print(stones[1] - stones[0])    
        return

    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i+1, i+k+1):
            try:
                dp[j] = min(
                        dp[i] + abs(stones[j] - stones[i]), 
                        dp[j]
                    )
            except:
                pass
        
    print(dp[n-1])

solve()