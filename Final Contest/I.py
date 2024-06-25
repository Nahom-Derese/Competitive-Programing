def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return  prefix



def solve():
    n,k = [int(i) for i in input().split()]
    nums=[0]*52
    test = [0]*52
    queries = set()
    ans = float("inf")

    for _ in range(n):
        l,r  = [int(i) for i in input().split()]
        queries.add((l,r))
        nums[l] += 1
        nums[r+1] -= 1
        if l>k or r<k:
            test[l]+=1
            test[r+1]-=1
        for i in range(1,52):
            nums[i]+=nums[i-1]
            test[i]+=test[i-1]
        for j in range(52):
            if nums[j]!=0:
                ans = min(ans,nums[j]-test[j])
                
    if ans < nums[k]:
        return True
    else:
        return False
                
            
            

    

    
    # if u and len(queries) > 1:
    #     return True

    # x.sort()
    # x = set(x)


    # for i in x:
    #     if i < u and i != 0:
    #         return True

    return False

    #     for i in range(l,r+1):
    #         if l<=k<=r:
    #             nums[i][1]=True
    #         nums[i][0]+=1
    # # print(nums)
    # for i in range(51):
    #     if nums[k][0]>nums[i][0] and nums[i][0]!=0:
    #         return True
    #     elif nums[i][1]==False and nums[i][0]!=0 and nums[k][0]!=0:
    #         return True
    # return False

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")


