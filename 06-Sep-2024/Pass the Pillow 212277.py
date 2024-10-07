# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        layer = time // (n-1)
       
        if layer % 2:
            return n - time % (n-1)
        
        return (time % (n-1)) + 1