for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    l = 0
    r = len(nums) - 1

    while l < r-1:
        if nums[l] == nums[l+1]:
            l += 1
        else:
            break
    
    while r > 1:
        if nums[r] == nums[r-1]:
            r -= 1
        else:
            break
    
    print(nums[l], nums[r])
    if(nums[l] == nums[r]):
        max(r-l, 0)
    

    print(max(l, n-r))