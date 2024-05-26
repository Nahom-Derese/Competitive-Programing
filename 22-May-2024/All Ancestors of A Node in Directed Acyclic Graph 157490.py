# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for node1, node2 in edges:
            graph[node1].append(node2)
            indegree[node2]+=1


        def topsort(multisource):
            res = [set() for _ in range(n)]
            queue = deque(multisource)

            while queue:
                x = queue.popleft()

                for node in graph[x]:
                    indegree[node]-=1
                    
                    # give previous ancestors to the child
                    res[node].add(x)
                    res[node].update(res[x])

                    if indegree[node]:
                        continue
                    queue.append(node)
            for i in range(len(res)):
                res[i] = sorted(res[i])
            return res

        multi_source = [i for i in range(n) if not indegree[i]]

        return topsort(multi_source)