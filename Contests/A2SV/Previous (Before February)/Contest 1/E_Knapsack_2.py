N, W = [int(i) for i in input().split()]
items = []
max_val = 0

for _ in range(N):
    w, v = [int(x) for x in input().split()]
    items.append((w,v))
    max_val+=v

def solve(max_val):
    dp = [float("inf") for _ in range(max_val+1)]
    dp[0] = 0

    for i in range(N):
        current_weight, current_value = items[i]
        for value in range(max_val, current_value-1, -1):
            idx = value - current_value
            dp[value] = min(dp[idx] + current_weight, dp[value])

    # print(dp)
    for i in range(-1, -len(dp)-1, -1):
        if dp[i] < W+1:
            return max_val + (i + 1)

print(solve(max_val))