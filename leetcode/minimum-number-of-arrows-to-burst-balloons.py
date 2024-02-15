class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])

        count = 1
        _range = points[0]
        for i,j in points[1:]:
            print(_range)
            if i <= _range[1]:
                _range[0]=i
                _range[1]=min(_range[1], j)
            else:
                _range = [i,j]
                count+=1
        return count