# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nodes = set(list(range(n)))
        dependent_nodes = set()
        for n1, n2 in edges:
            dependent_nodes.add(n2)
        
        independent_nodes = nodes - dependent_nodes

        if len(independent_nodes) == 1:
            return list(independent_nodes)[0]
        return -1