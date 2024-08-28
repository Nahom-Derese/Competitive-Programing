class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = ans = 0
        r = len(nums)-1

        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > k:
                r-=1
            elif cur_sum < k:
                l+=1
            else:
                ans += 1
                r-=1
                l+=1

        return ans
                