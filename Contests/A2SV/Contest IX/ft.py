n=int(input())
nums=[int(i) for i in input().split()]
tar = int(input())
left=0
right=n
for i in range(n):
    left+=1
    right-=1
    while left< n:

        
        sum = nums[left]+nums[right]
        
        if sum==tar:
            print("yes")
            break 
        else:
            print("No")
            break        
        right+=1
