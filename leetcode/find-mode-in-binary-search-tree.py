class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = Counter()

        def traverse(node):
            if node:
                nodes[node.val]+=1
                traverse(node.left)
                traverse(node.right)

        traverse(root)

        highest = max(nodes.values())

        return [k for k, v in dict(nodes).items() if v == highest]