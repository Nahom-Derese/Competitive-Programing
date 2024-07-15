def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


def solve():
    n, k = [int(i) for i in input().split()]
    
    nums = [0]*55

    for _ in range(n):
        l, r = [int(i) for i in input().split()]
        if k >= l and k <= r:
            nums[l]+=1
            nums[r+1]-=1
        
    nums = prefix_sum(nums)

    return nums[k] > nums[k+1] and nums[k] > nums[k-1]
        

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")
