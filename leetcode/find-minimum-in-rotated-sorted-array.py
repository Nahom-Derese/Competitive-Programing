class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1

        first = nums[0]

        while l <= r:
            middle = l + (r - l) // 2
            if middle and nums[middle] > first:
                l = middle + 1
            else:
                if r - l  == 1:
                    return min(nums[l], nums[r])
                if nums[middle] < nums[middle-1]:
                    return nums[middle]
                else:
                    r = middle - 1
        
        return nums[0]