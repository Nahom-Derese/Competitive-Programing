class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre_sum = [[0] + matrix[i-1] if i != 0 else [0] * (len(matrix[0])+1) for i in range(len(matrix)+1)]
        
        for i in range(1, len(self.pre_sum)):
            for j in range(1, len(self.pre_sum[0])):
                self.pre_sum[i][j] = self.pre_sum[i-1][j] + self.pre_sum[i][j-1] - self.pre_sum[i-1][j-1] + self.matrix[i-1][j-1]
        print(self.pre_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2+1][col2+1] - self.pre_sum[row1][col2+1] - self.pre_sum[row2+1][col1] + self.pre_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)