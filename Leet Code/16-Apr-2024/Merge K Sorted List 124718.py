# Problem: Merge K Sorted List - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        ans = dummy

        merged = []
        for i in lists:
            itr = i
            while itr:
                heappush(merged, itr.val)
                itr = itr.next
        
        while merged:
            ans.next = ListNode(heappop(merged))
            ans = ans.next
        
        return dummy.next