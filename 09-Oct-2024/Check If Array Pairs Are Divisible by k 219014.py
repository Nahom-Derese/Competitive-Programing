# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        x = sorted([num % k for num in arr])
        l = 0

        while l < n and not x[l]:
            l+=1
            
        if l % 2 != 0:
            return False

        for i in range(l, n):
            if x[i] + x[n-i+l-1] != k:
                return False

        return True