# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs(pp, qq):
            if pp and qq:
                print(pp.val, qq.val)
                if pp.val == qq.val:
                    u = dfs(pp.left, qq.left)
                    b = dfs(pp.right, qq.right)
                    return u and b
                else:
                    return False
            return not (pp or qq)

        return dfs(p,q)
                