# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        XOR = nums[0]
        for i in nums[1:]:
            XOR^=i
        
        ans = 0
        while XOR or k:
            if (XOR & 1) ^ (k & 1):
                ans+=1
            
            XOR>>=1
            k>>=1
        
        return ans