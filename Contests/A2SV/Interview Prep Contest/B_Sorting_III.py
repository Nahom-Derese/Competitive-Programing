from collections import defaultdict



def solve(nums):
    nums.sort(reverse=True)
    return nums


for _ in range(int(input())):
    n = int(input())
    
    nums = [int(i) for i in input().split()]

    print(*solve(nums))
