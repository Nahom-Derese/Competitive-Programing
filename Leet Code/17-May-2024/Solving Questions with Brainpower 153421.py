# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(idx):
            if idx >= len(questions):
                return 0

            x = questions[idx][0] + dp(idx + 1 + questions[idx][1])
            y = dp(idx + 1)

            return max(x,y)

        return dp(0)