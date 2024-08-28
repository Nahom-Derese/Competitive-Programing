# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        ans = 0

        nums = []
        while fast and fast.next:
            nums.append(slow.val)
        
            fast = fast.next.next
            slow = slow.next

        while slow:
            ans = max(nums.pop() + slow.val, ans)
            slow = slow.next
        

        return ans