
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        u = 0
        for j in nums:
            if j%2 == 0:
                u += j
        for i in queries:
            a = nums[i[1]]%2 == 0
            c = nums[i[1]]
            nums[i[1]] = nums[i[1]] + i[0]
            b = nums[i[1]]%2 == 0
            d = nums[i[1]]
            if a:
                if not b:
                    u -= c
                else:
                    u += d - c
            else:
                if not b:
                    pass
                else:
                    u += d
            
            ans.append(u)
        print(ans)
         
        
# Solution.sumEvenAfterQueries(Solution,[1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]])