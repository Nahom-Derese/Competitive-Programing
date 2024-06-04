# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [0]
        for i in nums:
            prefix_xor.append(prefix_xor[-1]^i)
        
        ans = []
        for i in range(1, len(nums)+1):
            current_ans = 0
            num = prefix_xor[-i]
            for j in range(maximumBit):
                if not (num & 1):
                    current_ans |= 1 << j
                num >>= 1

            ans.append(current_ans)
        return ans