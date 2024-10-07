def solve():
    n = int(input())
    
    nums = [int(i) for i in input().split()]
    
    ans = itr = 0

    while itr < n:
        x = nums[itr]
        count = 0
        while itr < n and nums[itr] == x:
            itr+=1
            count+=1
        ans = max(ans, count)
    
    print(ans)


for _ in range(int(input())):
    solve()
