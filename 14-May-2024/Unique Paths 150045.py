# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1,0),(0,1)]

        def inbound(row, col):
            return -1 < row < m and -1 < col < n

        def neigh(row, col):
            for r,c in directions:
                if inbound(row+r, col+c):
                    yield (row+r, col+c)


        @cache
        def dp(row, col):
            
            if (row, col) == (m-1,n-1):
                return 1

            ways = 0
            for new_row, new_col in neigh(row, col):
                ways += dp(new_row, new_col)
            
            return ways

        return dp(0,0)