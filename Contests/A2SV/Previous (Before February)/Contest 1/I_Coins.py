x = int(input())
nums = list(map(float, input().split()))
ans = 0

half = x//2

# for i in range(1 << x):
#     if i.bit_count() > half:
#         local_ans = 1
#         itr = x - 1
#         while itr > -1:
#             if i & 1: local_ans *= nums[itr]
#             else: local_ans *= (1 - nums[itr])
#             i >>= 1
#             itr-=1
#         ans += local_ans

# print(ans)

dp = [[0 for i in range(half+ 2)] for j in range(x+2)]

for i in range(1, half + 2):
    dp[0][i] = 1

for i in range(1, x+1):
    for j in range(1, half+2):
        dp[i][j] += dp[i-1][j] * nums[x-i-1]
        dp[i][j] += dp[i-1][j-1] * (1-nums[x-i-1])

print(dp[x][half+1].__round__(10))
