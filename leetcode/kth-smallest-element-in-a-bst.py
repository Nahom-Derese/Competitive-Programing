class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list_ = []

        def dfs(node):
            if node:
                dfs(node.left)
                list_.append(node.val)
                dfs(node.right)
        
        dfs(root)
        list_.sort()
        return list_[k-1]