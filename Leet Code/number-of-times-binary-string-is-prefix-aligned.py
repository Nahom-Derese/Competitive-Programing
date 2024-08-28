class Solution:
    def summation(self, n):
        return (n) * (n + 1) / 2

    def numTimesAllBlue(self, flips: List[int]) -> int:
        r = summ = 0
        
        ans = 0
        while r < len(flips):
            summ += flips[r]

            if self.summation(r+1) == summ:
                ans += 1
            
            r+=1

        return ans