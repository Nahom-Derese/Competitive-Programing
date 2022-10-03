import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined = [*nums1,*nums2]
        combined.sort()
        median = (combined[len(combined)//2 - 1] + combined[len(combined)//2]) / 2 if len(combined) % 2 == 0 else combined[len(combined)//2]
        return float('{:.5f}'.format(median))

# print (Solution.findMedianSortedArrays(Solution, [1,3],[2,4]))