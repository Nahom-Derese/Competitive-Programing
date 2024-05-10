# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        x = 1
        y = 1

        for i in range(n-1):
            temp = y
            y += x
            x = temp

        return y