# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

import sys


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            if n % 2 == 0:
                return self.myPow(x , n // 2) **2
            return self.myPow(x , n + 1) * 1 / x
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x , n // 2) **2
            return self.myPow(x , n - 1) * x
