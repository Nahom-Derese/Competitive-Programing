class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc(speed):
            ans = 0
            for i in piles:
                ans += ceil(i/speed)
            return ans
        
        l = 1
        r = max(piles)

        best = float("inf")

        while l <= r:
            middle = l + (r - l) // 2
            x = calc(middle)
            if  x <= h:
                r = middle - 1
            else:
                l = middle + 1

        return l