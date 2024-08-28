# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def rec(node):
            if node == None:
                return
            
            if node.children != None:
                for child in node.children:
                    rec(child)

            ans.append(node.val)
            
        rec(root)
        return ans