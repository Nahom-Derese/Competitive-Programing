class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]
        n = len(nums)
        def back(index, listt):
            
            for i in range(index, n):
                listt.append(nums[i])
                ans.append(listt[:])
                back(i+1, listt)
                listt.pop()
        
        back(0, [])

        return ans