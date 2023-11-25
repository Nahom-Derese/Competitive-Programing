t = int(input())

for i in range(t):
    n = int(input())

    nums = [int(i) for i in input().split()]

    val = 0
    possible = True

    for i in range(n):
        left = i-1
        right = i+1
        if left < 0:
            left = 0
        if right > n-1:
            right = 0
        
        if left != 0 and right != 0:
            if nums[right] > nums[i] and (nums[left] > nums[i] or possible):
                val+=1
            if nums[left] > nums[i] and nums[right] == nums[i]:
                possible = True
            if nums[left] == nums[i] and nums[right] != nums[i]:
                possible = False
            if nums[left] < nums[i] or nums[right] > nums[i]:
                possible = False
            

        else:
            if left == 0 and (nums[right] > nums[i]):
                val+=1
            elif right == 0 and (nums[left] > nums[i] or possible):
                val+=1
            
    
    if val == 1:
        print("YES")
    else:
        print("NO")
            
            
