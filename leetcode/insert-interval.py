class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals):
            intervals.insert(bisect_right(list(map(lambda x:x[0], intervals)), newInterval[0]), newInterval)
            merged = [intervals[0]]

            
            for i in range(1, len(intervals)):
                
                if intervals[i][0] <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], intervals[i][1])
                else:
                    merged.append(intervals[i])
            
            return merged
        else:
            return [newInterval]
