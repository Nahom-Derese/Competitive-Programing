# Definition for singly-linked list.
from re import S


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        itr = list1
        itr2 = list2
        ans = ListNode()
        itr3 = ans
        while itr != None and itr2 != None:
            if itr.val > itr2.val:
                itr3.next = ListNode(itr2.val)
                itr2=itr2.next
            else:
                itr3.next = ListNode(itr.val)
                itr=itr.next
            itr3 = itr3.next
        if itr != None:
            itr3.next = itr
        else:
            itr3.next = itr2
        return ans.next
                
    

# l1 = ListNode(1,ListNode(5,ListNode(9,ListNode(10,None))))
# l2 = ListNode(1,ListNode(2,ListNode(3,ListNode(6,None))))
# Solution.mergeTwoLists(Solution,l1,l2)