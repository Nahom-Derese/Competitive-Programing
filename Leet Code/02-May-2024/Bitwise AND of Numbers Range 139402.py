# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right and left > 0 and right > 0:
            left >>= 1
            right >>= 1
            count += 1
        if left and right:
            return left << count
        return 0