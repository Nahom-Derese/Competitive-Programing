# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = ans = 0
        r = len(nums) - 1

        while r > l:
            if nums[r] + nums[l] > k:
                r-=1
                continue
            elif nums[r] + nums[l] < k:
                l+=1
                continue
            
            ans+=1
            l+=1
            r-=1

        return ans