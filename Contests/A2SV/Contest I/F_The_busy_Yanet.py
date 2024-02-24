for _ in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    min_index = nums.index(min(nums))

    _sorted = True
    for i in range(min_index, n-1):
        if nums[i] > nums[i+1]:
            _sorted = False
            break
    
    if _sorted:
        print(min_index)
    else:
        print(-1)