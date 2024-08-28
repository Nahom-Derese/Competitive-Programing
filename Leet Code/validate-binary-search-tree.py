class Solution:
    def isValidBST(self, root: Optional[TreeNode], range_ = (float("-inf"), float('inf'))) -> bool:
        if not root:
            return True

        left = right = True

        with_in_range = root.val > range_[0] and root.val < range_[1]

        if with_in_range:
            left = self.isValidBST(root.left, (range_[0], root.val))
            right = self.isValidBST(root.right, (root.val, range_[1]))
            return left and right

        return False
