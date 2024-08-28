# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sortedList = SortedList([])
        ans = []
        for i in nums[::-1]:
            ans.append(sortedList.bisect_left(i))
            sortedList.add(i)
            
        return ans[::-1]