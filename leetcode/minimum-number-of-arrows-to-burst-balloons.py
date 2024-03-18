class Solution:
    def findMinArrowShots(self, points):
        points.sort()

        itr = ans = 0
        while itr < len(points):
            temp = itr
            while itr < len(points) and points[temp][1] >= points[itr][0]:
                if points[temp][1] > points[itr][1]:
                    temp = itr
                itr+=1
            ans+=1

        return ans