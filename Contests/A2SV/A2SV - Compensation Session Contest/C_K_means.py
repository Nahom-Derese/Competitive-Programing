from collections import Counter


def count_pairs(nums, x):
    pairs = 0
    seen = Counter()

    for num in nums:
        pairs += seen[x - num] 
        seen[num] += 1

    return pairs
        

def solve():
    n = int(input())
    nums = [int(i) for i in input().split()]
    total = sum(nums)
    
    target_mean = total / n
    target_sum = target_mean * 2

    ans = count_pairs(nums, target_sum)

    return ans

    
    

for _ in range(int(input())):
    print(solve())
