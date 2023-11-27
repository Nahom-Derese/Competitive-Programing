
for i in range(int(input())):
    n, summ = [int(i) for i in input().split()]

    nums = [int(i) for i in input().split()]

    left_ptr = 0
    right_ptr = 0

    ans = n
    summation = nums[0]

    while left_ptr <= right_ptr and right_ptr < len(nums) and left_ptr < len(nums):
        lengthOfSubarray = right_ptr - left_ptr + 1

        if summation == summ:
            if ans > n - lengthOfSubarray:
                ans = n - lengthOfSubarray
            right_ptr+=1
            try:
                if nums[right_ptr] == 1:
                    summation += 1
            except:
                pass
        elif summation > summ:
            if nums[left_ptr] == 1:
                summation -= 1
            left_ptr+=1
        elif summation < summ:
            right_ptr+=1
            try:
                if nums[right_ptr] == 1:
                    summation += 1
            except:
                pass
        

    if ans == n:
        print(-1)
    else:
        print(ans)