class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        diff = float("inf")
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            
            newTarget = target -  nums[i]

            while l < r:
                currentDiff = newTarget - (nums[l] + nums[r])

                if currentDiff > 0:
                    l+=1
                    if abs(diff) > abs(currentDiff):
                        diff = currentDiff
                elif currentDiff < 0:
                    r-=1
                    if abs(diff) > abs(currentDiff):
                        diff = currentDiff
                else:
                    return target

        
        return target - diff