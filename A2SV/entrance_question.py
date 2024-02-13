def prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]
    return prefix[1:]

def widest_sum(nums1, nums2):
    prefix_sum_1 = prefix_sum(nums1)
    prefix_sum_2 = prefix_sum(nums2)

    left = right = 0
    windowSize = 0
    maxWindowSize = 0
    diff = []

    


