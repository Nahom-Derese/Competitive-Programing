from collections import defaultdict

n = int(input())
nums = [int(i) for i in input().split()]

ans = sorted(list(zip(nums, list(range(1, n+1)))))

for i in range(n//2):
    print(ans[i][1], ans[n-i-1][1])