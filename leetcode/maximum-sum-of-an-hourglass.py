class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pre_sum = [[0]*(len(grid[0])+1) for i in range(len(grid)+1)]

        for i in range(1, len(pre_sum)):
            for j in range(1, len(pre_sum[0])):
                pre_sum[i][j] = grid[i-1][j-1] + pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]

        ans = 0
        for i in range(3, len(pre_sum)):
            for j in range(3, len(pre_sum[0])):
                current_sum = pre_sum[i][j] - pre_sum[i-3][j] - pre_sum[i][j-3] + pre_sum[i-3][j-3]
                current = current_sum - grid[i-2][j-1] - grid[i-2][j-3]
                
                ans = max(ans, current)

        return ans