for i in range(int(input())):
    o = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    l = 0
    r = 1
    ans = 1
    while r < o:
        diff =  nums[r] - nums[l]

        if diff > o-1 or r - l > o - 1 or diff == 0:
            l+=1
        
        ans = max(ans, r-l+1)
        
        r+=1

    print(ans)