# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        ans = 0
        for i, person in enumerate(happiness):
            ans+=max(person-i, 0)
            if i == k-1:
                break
        return ans