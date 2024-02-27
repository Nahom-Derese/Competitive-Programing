# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def tree(node):
            if node == None:
                return 0
            

            ans = 0
            ans+=tree(node.left)
            ans+=tree(node.right)
                
            if node.val >= low and node.val <= high:
                ans+=node.val
            
            return ans

        return tree(root)

