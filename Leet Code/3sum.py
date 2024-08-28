class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            target = -nums[i]

            while r > l:
                summ = nums[l] + nums[r]
                if summ > target:
                    r-=1
                elif summ < target:
                    l+=1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    r-=1

        return list(ans)
            
        
