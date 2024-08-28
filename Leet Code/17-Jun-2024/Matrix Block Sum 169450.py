# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                mat[i][j] += mat[i-1][j] if i>0 else 0
                mat[i][j] += mat[i][j-1] if j>0 else 0
                mat[i][j] -= mat[i-1][j-1] if i>0 and j>0 else 0
        
        ans = [ [0]*m for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                mi, mj  = min(n-1,i+k), min(m-1,j+k)
                mini = 0 if i-k-1<0 or j-k-1<0 else mat[i-k-1][j-k-1]
                left = mat[mi][j-k-1] if j-k-1 >=0 else 0
                right = mat[i-k-1][mj] if i-k-1 >=0 else 0
                ans[i][j] = mat[mi][mj]+mini-left-right

        return ans