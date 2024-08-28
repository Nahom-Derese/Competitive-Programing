# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        itr = head
        itr2 = head.next
        itr3 = head.next
        while itr and itr.next and itr.next.next:
            itr.next = itr.next.next
            itr = itr.next
            itr2.next = itr2.next.next
            itr2 = itr2.next
        
        if itr:
            itr.next = itr3
        return head

