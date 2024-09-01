# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])

        def inbound(row, col):
            return 0 <= row < M and  0 <= col < N

        def neighbours(row, col):
            for dir_y, dir_x in [(1, 0), (0, 1)]:
                new_row = row + dir_y
                new_col = col + dir_x

                if inbound(new_row, new_col):
                    yield (new_row, new_col)

        @cache
        def dp(row, col):
            if row == M-1 and col == N-1:
                return grid[row][col]

            res = float("inf")

            for new_row, new_col in neighbours(row, col):
                res = min(
                    dp(new_row, new_col) + grid[row][col],
                    res
                ) 

            return res

        return dp(0,0)