# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        while node:
            if node.next:
                node.val = node.next.val
                if not node.next.next:
                    node.next = None
            node = node.next

        