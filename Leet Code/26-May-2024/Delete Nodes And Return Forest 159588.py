# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        ans = []

        def rec_delete(node):
            if node.val in to_delete:
                if node.left:
                    x = rec_delete(node.left)
                    if x:
                        ans.append(x)
                if node.right:
                    x = rec_delete(node.right)
                    if x:
                        ans.append(x)
                return None

            if node.left:
               node.left = rec_delete(node.left)
            if node.right:
               node.right = rec_delete(node.right)

            return node

        x = rec_delete(root)
        if x:
            ans.append(x)
        return ans