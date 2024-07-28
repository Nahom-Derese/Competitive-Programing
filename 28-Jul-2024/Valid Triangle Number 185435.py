# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        v = sorted(n for n in nums if n > 0)
        return sum(
            bisect_left(v, v[i] + v[j]) - j - 1
            for i in range(len(v) - 2)
            for j in range(i + 1, len(v) - 1)
        )