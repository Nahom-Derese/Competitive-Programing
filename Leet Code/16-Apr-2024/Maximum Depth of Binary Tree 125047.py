# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dfs(node, depth):
            nonlocal ans
            if node:
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
            else:
                ans = max(ans, depth)

        dfs(root, 0)
        return ans