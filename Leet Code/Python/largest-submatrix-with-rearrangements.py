from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 1:
                    if j-1 > -1:
                        matrix[j][i] += matrix[j-1][i]

        for j in range(len(matrix)):
            matrix[j] = sorted(matrix[j])
        
        ans = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0 and (len(matrix[i]) - j) * (matrix[i][j]) > ans:
                    ans = (len(matrix[i]) - j) * (matrix[i][j])
                    
        return ans


print(Solution.largestSubmatrix(Solution,[[0,0,1],[1,1,1],[1,0,1]]))
print(Solution.largestSubmatrix(Solution,[[1,0,1,0,1]]))
print(Solution.largestSubmatrix(Solution, [[1,1,0],[1,0,1]]))