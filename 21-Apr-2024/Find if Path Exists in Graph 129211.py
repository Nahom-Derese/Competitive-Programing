# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj_list = defaultdict(list)

        for s, d in edges:
            adj_list[s].append(d)
            adj_list[d].append(s)
        
        visited = set()
        
        def dfs(node):
            nonlocal adj_list
            nonlocal visited

            queue = [node]


            while queue:
                x = queue.pop()
                if x == destination:
                    return True
                visited.add(x)
                for child in adj_list[x]:
                    if child not in visited:
                        queue.append(child)
                        if child == destination:
                            return True

            return False
        
        return dfs(source)