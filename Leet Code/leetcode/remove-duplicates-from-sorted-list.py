# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        if not itr:
            return None
        while itr and itr.next:
            itr2 = itr
            while itr2 and itr2.next and itr2.val == itr2.next.val:
                itr2 = itr2.next
            itr.next = itr2.next
            itr = itr.next

        return head