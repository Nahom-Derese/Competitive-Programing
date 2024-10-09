# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        
        L = 0
        T = 0
        R = n
        B = m

        while head:
            for i in range(L, R):
                if not head:
                    return matrix
                matrix[T][i] = head.val
                head = head.next
            T += 1
        
            for i in range(T, B):
                if not head:
                    return matrix
                matrix[i][R-1] = head.val
                head = head.next
            R -= 1
        
            for i in range(R-1, L-1, -1):
                if not head:
                    return matrix
                matrix[B-1][i] = head.val
                head = head.next
            B -= 1

            for i in range(B-1, T-1, -1):
                if not head:
                    return matrix
                matrix[i][L] = head.val
                head = head.next
            L += 1
        

        return matrix