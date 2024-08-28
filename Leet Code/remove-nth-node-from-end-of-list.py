# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        itr1 = dummy
        itr2 = dummy

        while n != 0:
            itr2 = itr2.next
            n-=1
        
        while itr2.next:
            itr1 = itr1.next
            itr2 = itr2.next

        if itr1.next:
            itr1.next = itr1.next.next
        else:
            itr1.next = None


        return dummy.next