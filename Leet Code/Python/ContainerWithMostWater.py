class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        r = len(height)-1
        l = 0
        while r != l:
            maxArea = max(maxArea, min(height[l], height[r]) * (r-l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxArea
            
print (Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))
        