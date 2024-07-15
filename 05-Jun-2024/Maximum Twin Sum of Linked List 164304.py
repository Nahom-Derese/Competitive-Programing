# Problem: Maximum Twin Sum of Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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