# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        def prefix_sum(arr):
            n = len(arr)
            prefix = [0] * n
            prefix[0] = arr[0]
            for i in range(1, n):
                prefix[i] = prefix[i - 1] + arr[i]
            return [0] + prefix[:-1]

        def suffix_sum(arr):
            n = len(arr)
            suffix = [0] * n
            suffix[n - 1] = arr[n - 1]
            for i in range(n - 2, -1, -1):
                suffix[i] = suffix[i + 1] + arr[i]
            return suffix[1:] + [0]
        
        


        suffix = suffix_sum(nums)
        prefix = prefix_sum(nums)

        for i in range(len(nums)):
            if suffix[i] == prefix[i]:
                return i

        return -1