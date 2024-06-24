# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        one_size, two_size, write_pos = m-1, n-1, n+m-1


        while two_size >= 0:
            if one_size >= 0 and nums1[one_size] > nums2[two_size]:
                nums1[write_pos] = nums1[one_size]
                one_size -= 1
            else:
                nums1[write_pos] = nums2[two_size]
                two_size -= 1
            write_pos -= 1