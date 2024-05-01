# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1


        return ans