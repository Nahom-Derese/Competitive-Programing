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
                if a and a[-1] == '-':
                    a.pop()
                else:
                    a.append('-')
        
        def inorder(node):
            nonlocal b
            if node:
                b.append(node.val)
                inorder(node.left)
                inorder(node.right)
            else:
                if b and b[-1] == '-':
                    b.pop()
                else:
                    b.append('-')
            
        postorder(root.left)
        inorder(root.right)
     
        return b == a