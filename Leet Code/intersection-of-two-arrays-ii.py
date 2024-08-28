class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c_1 = Counter(nums1)
        c_2 = Counter(nums2)

        ans = []
        for i in c_1:
            if i in c_2:
                ans.extend([i] * min(c_1[i], c_2[i]))

        return ans