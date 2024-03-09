# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        itr = dummy
        while itr:
            itr2 = itr
            while itr2 and itr2.val == itr.val:
                itr2 = itr2.next
            itr.next = itr2
            itr = itr2
        return head