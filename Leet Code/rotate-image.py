class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ans = []
        for i,j in enumerate(zip(*matrix)):
            matrix[i] = list(reversed(j))