# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        
        prefix_cnt = Counter()
        prefix_sum = defaultdict(int)
        
        
        for i, n in enumerate(nums):
            prefix_sum[n] += i
            prefix_cnt[n] += 1
            ans[i] += prefix_cnt[n]*i-prefix_sum[n]

        suffix_cnt = Counter()
        suffix_sum = defaultdict(int)
        
        
        for i, n in reversed(list(enumerate(nums))):
            suffix_sum[n] += i
            suffix_cnt[n] += 1
            ans[i] += suffix_sum[n]-suffix_cnt[n]*i

        return ans