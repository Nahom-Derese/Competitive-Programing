# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []

        while list1 and list2:
            if list1.val > list2.val:
                ans.append(list2.val)
                list2 = list2.next
            else:
                ans.append(list1.val)
                list1 = list1.next
                
        while list1:
            ans.append(list1.val)
            list1 = list1.next
        while list2:
            ans.append(list2.val)
            list2 = list2.next

        dummy = ListNode()
        itr = dummy
        for val in ans:
            itr.next = ListNode(val)
            itr = itr.next

        return dummy.next