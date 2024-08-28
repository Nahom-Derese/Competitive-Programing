from math import ceil

n = int(input())

m = int(input())

nums = []

def solve(n, m, nums):
    ans = []
    nums.sort()
    
    mx, mi = nums[-1], nums[0]
    
    # maximum calc
    ans.append(mx + m)
    
    # minimum calc
    minimum_needed = sum([mx - num for num in nums])
    
    if m <= minimum_needed:
        ans.append(mx)
        return ans[::-1]

    m -= minimum_needed

    q, r = divmod(m, n)
    
    max_ans = mx + q
    if r:
        max_ans+=1
    
    ans.append(max_ans)

    return ans[::-1]

for _ in range(n):
    nums.append(int(input()))

print(*solve(n, m, nums))
