class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k

        summ = sum(nums[:k])
        ans = summ
        while r < len(nums):
            summ+=nums[r]
            summ-=nums[l]
            ans = max(ans, summ)
            r+=1
            l+=1

        return ans/k
        