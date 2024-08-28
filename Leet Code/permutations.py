class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def permutate(index):
            if index == len(nums):
                ans.append(nums[:])
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permutate(index+1)
                nums[index], nums[i] = nums[i], nums[index]

        permutate(0)

        return ans