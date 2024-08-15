# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        i = 0
        
        stack = [ intervals[0] ]
        
        while i < len(intervals):
            while i < len(intervals) and stack and stack[-1][1] >= intervals[i][0] and stack[-1][1] <= intervals[i][1]:
                x,y = stack.pop()
                stack.append([x, intervals[i][1]])
                i+=1

            if i < len(intervals) and stack[-1][1] <= intervals[i][1]:
                stack.append(intervals[i])
            
            i+=1

        return stack