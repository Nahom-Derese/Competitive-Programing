t = int(input())

for i in range(t):
    n = int(input())

    nums = [int(i) for i in input().split()]

    val = 0
    possible = True

    for i in range(n):
        right = i+1
        
        if right < len(nums):
            if nums[right] > nums[i]:
                val=1
            if val == 1 and nums[right] < nums[i]:
                possible = False
    
    if possible:
        print("YES")
    else:
        print("NO")