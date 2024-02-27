class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        f = s = 0
        while f < len(nums1) and s < len(nums2):
            if nums1[f] == nums2[s]:
                return nums1[f]
            if nums1[f] > nums2[s]:
                s+=1
            else:
                f+=1
        return -1