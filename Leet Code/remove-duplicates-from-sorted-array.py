class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first_pt = 0
        second_pt = 1

        # [0,0,1,1,1,2,2,2,3,5,6]
        while second_pt < len(nums):
            num1=nums[first_pt]
            num2=nums[second_pt]
            if num1 < num2:
                first_pt += 1
                nums[first_pt] = num2
            else:
                second_pt +=1
        
        return first_pt+1
            
