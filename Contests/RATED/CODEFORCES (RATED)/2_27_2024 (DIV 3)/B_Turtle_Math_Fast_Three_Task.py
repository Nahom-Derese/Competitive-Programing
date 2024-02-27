from itertools import accumulate

for i in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))
    x = sum(nums)
    
    if len(nums) == 1 and nums[0] % 3 != 0:
        print(1)

    elif x % 3 == 0:
        print(0)

    elif x % 3 == 2:
        print(1)
    else:
        for i in nums:
            if i%3 == 1:
                print(1)
                break
        else:
            print(2)
                
