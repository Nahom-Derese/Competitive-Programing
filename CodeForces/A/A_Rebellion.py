for i in range(int(input())):

    n = int(input())

    nums = list(map(int, input().split()))

    l=0
    r=n-1

    while l < r:
        if nums[l] > nums[r]:
            nums[r]+=nums[l]
            nums = nums[l+1:]
        
        r-=1
    
        

    print(nums)
