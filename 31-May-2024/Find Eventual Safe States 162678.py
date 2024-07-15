# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        order = []
        colors = [0 for _ in range(len(graph))]
        
        
        def topSort(node):
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for neighbor in graph[node]:
                if colors[neighbor] == 2:
                    continue
                if not topSort(neighbor):
                    return False
            
            
            colors[node] = 2
            order.append(node)
            return True

        for node in range(len(graph)):

            if colors[node] != 0:
                continue
            
            topSort(node)


        return sorted(order)