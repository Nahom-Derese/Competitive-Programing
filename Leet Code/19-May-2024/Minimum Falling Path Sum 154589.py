# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dirs = [(1,-1), (1, 0),  (1, 1)]
        
        def choices(row, col):
            for r,c in dirs:
                if -1 < row+r < len(matrix) and -1 < col+c < len(matrix[0]):
                    yield (row+r, col+c)

        @cache
        def dp(row, col):
            if row == len(matrix) - 1:
                return matrix[row][col]

            res = float("inf")
            for r, c in choices(row, col):
                res  = min(res, dp(r, c))
        
            return matrix[row][col] + res

        ans = float("inf")
        for i in range(len(matrix[0])):
            ans = min(ans, dp(0, i))

        
        return ans