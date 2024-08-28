# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        self.G = []
        for i in [0, 1]:
            self.G.append(defaultdict(set))
        
        for e0, e1 in redEdges:
            self.G[0][e0].add(e1)
        
        for e0, e1 in blueEdges:
            self.G[1][e0].add(e1)
            
        ans = [-1] * n
        visited = set()
        queue = deque([(0, 0, 0)])
        
        while queue:
            node, color, step = queue.popleft()
            if (ans[node] == -1) or (ans[node] > step):
                ans[node] = step
                
            visited.add((node, color))
            next_color = (color + 1) % 2
            for nn in self.G[next_color][node]:
                if (nn, next_color) not in visited:
                    queue.append((nn, next_color, step + 1))
            
        
        
        visited = set()
        queue = collections.deque([(0, 1, 0)])
        while queue:
            node, color, step = queue.popleft()
            if (ans[node] == -1) or (ans[node] > step):
                ans[node] = step
                
            visited.add((node, color))
            next_color = (color + 1) % 2
            for nn in self.G[next_color][node]:
                if (nn, next_color) not in visited:
                    queue.append((nn, next_color, step + 1))
        
        return ans