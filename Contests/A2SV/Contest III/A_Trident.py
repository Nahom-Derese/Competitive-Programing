def ans(n, nums):
    l = 0
    r = 2

    while r < n:
        if nums[l] < nums[l+1] and nums[l+1] > nums[r]:
            print("YES")
            print(l+1, l+2, r+1)
            return
        r+=1
        l+=1
    print("NO")
    return


for i in range(int(input())):
    n = int(input())

    nums = [int(i) for i in input().split()]

    ans(n, nums)
