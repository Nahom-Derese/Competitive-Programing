t = int(input())

for i in range(t):
    n = int(input())

    nums = [int(i) for i in input().split()]

    num_sorted = nums.copy()
    num_sorted.sort()

    ans = 0
    
    for i in range(n):
        if (num_sorted[i] % 2==0 and nums[i] % 2 == 0) or (num_sorted[i] % 2 != 0 and nums[i] % 2 != 0):
            ans += 1
        
    if ans == n:
        print("YES")
    else:
        print("NO")

        