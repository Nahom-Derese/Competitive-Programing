# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/


class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        inDegrees = Counter(edges)
        del(inDegrees[-1])

        def topologicalSort(start):
            queue = deque(start)

            while queue:
                node = queue.popleft()
                neighbour = edges[node]
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
                

        visited = set()
        def cycleLength(start):
            visited.add(start)
            queue = deque([start])
            level = 1

            while queue:
                boundary = len(queue)
                for _ in range(boundary):
                    node = queue.popleft()
                    neighbour = edges[node]
                    if neighbour in visited:
                        return level
                    
                    queue.append(neighbour)
                    visited.add(neighbour)
                level+=1

            return level
        
        
        topologicalSort([i for i in range(len(edges)) if inDegrees[i] == 0])
        ans = 0
        for i in range(len(edges)):
            if inDegrees[i] and edges[i] not in visited:
                ans = max(ans, cycleLength(i))
        return -1 if ans == 0 else ans