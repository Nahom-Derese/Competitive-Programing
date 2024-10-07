# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1),(0,0)]

        def max_neighbours(row,col):
            max_ = float("-inf")
            for r,c in directions:
                max_ = max(grid[row+r][col+c], max_)

            return max_

        N = len(grid)
        ans = [[0]*(N-2) for i in range(N-2)]
        
        for i in range(N-2):
            for j in range(N-2):
                ans[i][j] = max_neighbours(i+1, j+1)
        
        return ans