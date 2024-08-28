# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys

def solve(n, nums):
    ans = 0
    i=2
    while i < n+1:
        x = i//2
        for j in range(x, n+1, i):
            
            if abs(nums[j] - nums[j-x]) > x:
                return -1
            if nums[j-x] > nums[j]:
                ans+=1
                nums[j-x], nums[j] = nums[j], nums[j-x]
        i*=2
    return ans

for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    
    nums = [int(i) for i in sys.stdin.readline().split()]
    
    print(solve(n, nums))