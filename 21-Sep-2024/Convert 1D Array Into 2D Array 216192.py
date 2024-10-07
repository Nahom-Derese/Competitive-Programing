# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []

        N = len(original)

        if N != m*n:
            return res

        for i in range(0, N, n):
            res.append(original[i:i+n])

        return res