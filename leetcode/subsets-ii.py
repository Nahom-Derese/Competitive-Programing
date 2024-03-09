class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()
        def backtrack(idx, current):
            if len(current) > -1:
                ans.add(tuple(current))
                
            for i in range(idx, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current[:])
                x = current.pop()
                
        backtrack(0, [])

        return ans