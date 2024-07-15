# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        def prefix_sum(arr):
            n = len(arr)
            prefix = [0] * n
            prefix[0] = arr[0]
            for i in range(1, n):
                prefix[i] = prefix[i - 1] + arr[i]
            return [0] + prefix


        def suffix_sum(arr):
            n = len(arr)
            suffix = [0] * n
            suffix[n - 1] = arr[n - 1]
            for i in range(n - 2, -1, -1):
                suffix[i] = suffix[i + 1] + arr[i]
            return suffix + [0]


        pre = prefix_sum(nums)
        suf = suffix_sum(nums)

        ans = 0
        min_so_far = float("inf")
        for i in range(1, len(nums)+1):
            if (len(nums)-i) == 0:
                calc = (pre[i] // (i))
            else:
                calc = abs((pre[i] // (i)) - (suf[i] // (len(nums)-i)))
            
            if min_so_far > calc:
                min_so_far = calc
                ans = i-1
        
        return ans