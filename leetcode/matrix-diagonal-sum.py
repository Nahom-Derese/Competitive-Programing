class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        itr = (0,0)
        ans = 0
        for i,j in enumerate(range(n-1,-1,-1)):
            ans+=mat[i][i]
            if i != j:
                ans+=mat[i][j]
        return ans