# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        x = num.bit_length()
        return num ^ (1 << x)-1