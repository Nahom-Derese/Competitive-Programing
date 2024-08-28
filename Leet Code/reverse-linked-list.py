# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        itr = head
        temp = None

        while itr:
            x = itr.next
            itr.next = temp
            temp = itr
            itr=x
        
        return temp