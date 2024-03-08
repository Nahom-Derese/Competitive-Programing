class Solution:
    def minimumSteps(self, s: str) -> int:
        running_sum = 0
        ans = 0
        for i in s:
            if i == '1':
                running_sum += 1
            else:
                ans+=running_sum
        return ans