# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for i in nums:
            xor ^= i

        mask = xor & -xor

        num1, num2 = 0, 0

        for num in nums:
            if (num & mask) != 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]