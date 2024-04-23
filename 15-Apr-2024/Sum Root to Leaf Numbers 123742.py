# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, current):
            nonlocal ans
            if node:
                if not (node.left or node.right):
                    ans+=int(current+str(node.val))
                dfs(node.left, current+str(node.val))
                dfs(node.right, current+str(node.val))
            return ""

        dfs(root, "")            
        return ans