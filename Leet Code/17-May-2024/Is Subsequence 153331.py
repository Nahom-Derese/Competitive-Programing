# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False    

        # DP approach
        dp = [[1] * (len(t)+1)] + [[0] * (len(t)+1) for _ in range(len(s))]

        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                if dp[r][c-1]:
                    dp[r][c] = dp[r][c-1]
                elif s[r-1] == t[c-1]:
                    dp[r][c] = dp[r-1][c-1]
            
        return dp[-1][-1]