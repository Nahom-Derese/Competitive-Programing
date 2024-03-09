class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def findK(s):
            running_sum = 0
            m = 1
            for i in nums:
                running_sum += i
                if running_sum > s:
                    running_sum = i
                    m += 1
            return m

        start = max(nums)
        end = sum(nums)
        
        while start <= end:
            middle = start + (end - start) // 2

            val = findK(middle)
            
            if val > k:
                start = middle + 1
            elif val <= k:
                end = middle - 1

        return start