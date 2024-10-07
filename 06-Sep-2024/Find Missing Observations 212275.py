# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        sumOfNrolls  = (mean * (len(rolls) + n)) - sum(rolls)
        
        ans = [1] * n
        
        if int(sumOfNrolls) != sumOfNrolls:
            return []

        if (6*n) < sumOfNrolls or sumOfNrolls < n:
            return []

        current_sum = n
        sumOfNrolls -= current_sum
        i = 0

        while sumOfNrolls:
            x = min(sumOfNrolls, 5)
            ans[i] += x
            current_sum += x
            sumOfNrolls -= x

            i+=1

        return ans