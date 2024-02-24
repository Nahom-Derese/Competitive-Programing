for i in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-1] - nums[0])