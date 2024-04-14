# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])

        ans = []

        while queue:
            sum_level = 0
            boundary = len(queue)
            
            for _ in range(boundary):
                x = queue.popleft()
                sum_level += x.val
                
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            ans.append(sum_level / boundary)
        
        return ans


