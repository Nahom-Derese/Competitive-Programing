# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for person1, person2 in richer:
            graph[person1].append(person2)
            indegree[person2]+=1


        def topsort(multisource):
            res = [(quiet[i], i) for i in range(len(quiet))]
            queue = deque(multisource)

            while queue:
                x = queue.popleft()

                for node in graph[x]:
                    indegree[node]-=1
                    
                    # give previous ancestors to the child
                    res[node] = min((quiet[x], x), res[x], res[node])
                   

                    if indegree[node]:
                        continue
                    queue.append(node)
                    
            return res


        multi_source = [i for i in range(len(quiet)) if not indegree[i]]

        anscestors = topsort(multi_source)
        
        return [anscestors[i][1] for i in range(len(quiet))]