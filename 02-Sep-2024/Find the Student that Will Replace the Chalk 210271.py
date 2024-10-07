# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = [0]

        for c in chalk:
            prefix_sum.append(prefix_sum[-1] + c)

        remainder = k % prefix_sum[-1]
        
        return bisect_right(prefix_sum, remainder) - 1
