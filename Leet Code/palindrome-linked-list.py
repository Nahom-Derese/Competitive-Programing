# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = head
        b = ''
        while a.next != None:
            b+=str(a.val)
            a=a.next
        b+=str(a.val)
        if b == b[::-1]:
            return True
        else:
            return False