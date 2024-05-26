# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        DiGraph = list[list[int]]

        def flip_dir(g: DiGraph) -> DiGraph:
            r_graph = [[] for _ in range(len(graph))]
            r_edges = ((v, u) for u, vs in enumerate(graph) for v in vs)
            for u, v in r_edges: r_graph[u].append(v)
            return r_graph
        
        safeness = [False] * len(graph)
        out_degrees = {u: len(vs) for u, vs in enumerate(graph)}

        r_graph = flip_dir(graph)

        terminals = (u for u, d in out_degrees.items() if d == 0)
        frontier = deque(terminals)

        while frontier:
            u = frontier.popleft()
            safeness[u] = True
            for v in r_graph[u]: out_degrees[v] -= 1
            frontier.extend(filterfalse(out_degrees.get, r_graph[u]))
        
        return [u for u, is_safe in enumerate(safeness) if is_safe]

        # order = []
        # colors = [0 for _ in range(len(graph))]
        
        
        # def topSort(node):
        #     if colors[node] == 1:
        #         return False
            
        #     colors[node] = 1
        #     for neighbor in graph[node]:
        #         if colors[neighbor] == 2:
        #             continue
        #         if not topSort(neighbor):
        #             return False
            
            
        #     colors[node] = 2
        #     order.append(node)
        #     return True

        # for node in range(len(graph)):
        #     print(node)

        #     if colors[node] != 0:
        #         continue
            
        #     if not topSort(node):
        #         return []

        # print(colors)

        # return order