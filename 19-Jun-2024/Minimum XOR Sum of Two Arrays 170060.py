# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        precomputed = [[a[i] ^ b[j] for j in range(n)] for i in range(n)]
        @cache
        def dp(mask: int) -> int:
            i = bin(mask).count("1")
            if i >= n:
                return 0
            return min(precomputed[i][j] + dp(mask | (1 << j)) 
                       for j in range(n) if mask & (1 << j) == 0)
        return dp(0)