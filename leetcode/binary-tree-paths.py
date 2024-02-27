
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        
        def allPath(node, current):
            nonlocal ans

            if node:
                if current == "":
                    current += f'{node.val}'
                else:
                    current += f'->{node.val}'

                
                if (not node.left) and (not node.right):
                    ans.append(current)
                    return
                left = allPath(node.left, current)
                right = allPath(node.right, current)

        
        allPath(root, "")

        return ans

