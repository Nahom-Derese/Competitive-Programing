from collections import defaultdict

def solve():
    n = int(input())

    nums = [(int(j), i+1) for i,j in enumerate(input().split())]
    nums.sort()
    running_sum = itr = 0

    for i in range(n-1):
        running_sum+=nums[i][0]
        
        if running_sum < nums[i+1][0]:
            itr = i+1


    nums = list(map( lambda x:x[1] ,nums))[itr:]
    nums.sort()
    print(len(nums))
    print(*nums)

for _ in range(int(input())):
    solve()
