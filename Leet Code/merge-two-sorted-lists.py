# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        start = list1
        itr2 = list2
        if list1 and list2 and list1.val > list2.val:
            start = list2
            itr2 = list1
        
        head = start
        while start and start.next:
            if itr2 and start.next.val > itr2.val:
                s = start.next
                start.next = itr2
                itr2 = s
            start = start.next
        
        if start:
            start.next = itr2
        else:
            return itr2
        
        return head