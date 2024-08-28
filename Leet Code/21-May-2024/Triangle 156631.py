# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Top Down
        # def dp(row, col):
        #     if row == len(triangle):
        #         return 0
        #     return triangle[row][col] + min(dp(row+1, col), dp(row+1, col+1))
        # return dp(0,0)
        
        # Bottom Up
        dp = [[float("inf")]*i for i in range(1, len(triangle)+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(0, i):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j])
                dp[i][j+1] = min(dp[i][j+1], dp[i-1][j] + triangle[i][j+1])
        
        n = len(triangle)-1
        return min(dp[n])