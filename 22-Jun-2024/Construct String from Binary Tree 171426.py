# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def dfs(node):
            if not node:
                return ""

            res = f"{node.val}"
            
            if node.right or node.left:
                res += f"({dfs(node.left)})"

            if node.right:
                res += f"({dfs(node.right)})"

            return res

        return dfs(root)