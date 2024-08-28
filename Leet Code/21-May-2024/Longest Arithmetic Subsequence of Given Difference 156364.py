# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)

        for i in range(len(arr)):
            dp[arr[i]] = 1 + dp[arr[i] - difference]

        return max(dp.values())