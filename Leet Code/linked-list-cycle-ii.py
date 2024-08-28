# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def cycleExists(node):
            fast = slow = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return fast
            return None
        
        itr = head
        node = cycleExists(head)
        
        if node:
            while node != itr:
                node = node.next
                itr = itr.next

        return node