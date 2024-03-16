for i in range(int(input())):
    n = int(input())

    nums = [int(i) for i in input().split()]

    if not sum(nums) % 4:
        for r in range(1, n-1):
            if nums[r-1] < 0:
                print("NO")
                break
            temp = nums[r-1]
            nums[r-1] -= temp
            nums[r] -= 2 * temp
            nums[r+1] -= temp
        else:
            if abs(nums[-2]) or abs(nums[-1]):
                print("NO")
            else:
                print("YES")
    else:
        print("NO") 