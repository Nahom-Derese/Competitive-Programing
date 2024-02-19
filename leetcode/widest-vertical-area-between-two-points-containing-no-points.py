class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        y = sorted(points,key=lambda x: x[0])
        l=0
        r=1

        ans = 0

        while r < len(points):
            
            ans = max(ans, y[r][0] - y[l][0])

            l+=1
            r+=1
        
        return ans