# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head

        while itr:
            if not itr.val:
                temp = itr
                itr = itr.next
                while itr and itr.val:
                    temp.val += itr.val
                    itr = itr.next
                    
                if itr and itr.next:
                    temp.next = itr
                else:
                    temp.next = None
            
        return head