t = int(input())

for i in range(t):
    n = int(input())

    nums = [int(i) for i in input().split()]

    first = False

    ans = True

    for y in range(1,len(nums)):
        if nums[y] > nums[y-1]:
            first = True
        
        if first and nums[y] < nums[y-1]:
            ans = False
            break
    
    if ans:
        print("YES")
    else:
        print("NO")