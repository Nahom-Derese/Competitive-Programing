# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        # visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def neighbors(row, col):
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col) and matrix[row][col] < matrix[new_row][new_col]:
                    yield new_row, new_col

        @cache
        def dfs(row, col):
            max_path = 1
            for new_row, new_col in neighbors(row, col):
                max_path = max(1 + dfs(new_row, new_col), max_path)
            return max_path

        ans = 1
        for i in range(n):
            for j in range(m):
                ans = max(dfs(i,j), ans)

        return ans