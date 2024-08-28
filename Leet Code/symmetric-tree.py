# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        a = []
        b = []
        
        def postorder(node):
            nonlocal a
            if node:
                a.append(node.val)
                postorder(node.right)
                postorder(node.left)
            else:
                a.append('-')
        
        def preorder(node):
            nonlocal b
            if node:
                b.append(node.val)
                preorder(node.left)
                preorder(node.right)
            else:
                b.append('-')
            
        postorder(root.left)
        preorder(root.right)
     
        return b == a