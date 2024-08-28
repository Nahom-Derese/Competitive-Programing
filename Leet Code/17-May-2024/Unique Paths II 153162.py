# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range (m+1)]

        dp[0][1] = 1
        dp[1][0] = 0
        

        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1]:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]