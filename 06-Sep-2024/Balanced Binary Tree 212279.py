# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        stack.append((root, False))
        return_value=defaultdict(int)
        
        while stack:
            node,v=stack.pop()
            if v:
                left = return_value[node.left]
                right = return_value[node.right]
                
                if abs(left-right) > 1:
                    return False
                
                return_value[node] = max(left,right) + 1
            else:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
                if node.right:
                    stack.append((node.right,False))
                
        return True


