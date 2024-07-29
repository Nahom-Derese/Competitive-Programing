# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([root])
        levels = []

        while queue:
            level = []
            for i in range(len(queue)):
                x = queue.popleft()
                if x:
                    level.append(x.val)
                
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
            levels.append(level)     

        return [level[-1] for level in levels if level]
            