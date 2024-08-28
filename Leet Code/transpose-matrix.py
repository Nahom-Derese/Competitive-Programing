class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        # return transpose 
        return zip(*matrix)