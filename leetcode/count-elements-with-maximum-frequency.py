class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = Counter(nums)
        max_ = max(a.values())

        ans = 0
        for k, v in a.items():
            if v == max_:
                ans+=v
        
        return ans