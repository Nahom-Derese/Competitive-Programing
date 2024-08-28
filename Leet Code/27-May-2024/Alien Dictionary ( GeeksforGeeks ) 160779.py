# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from string import ascii_lowercase
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):

        strings = alien_dict
        alphabet = set(ascii_lowercase[:K])
        indegree = {i: 0 for i in alphabet}
        
        
        def solve():
            graph = defaultdict(list)
        
            for i in range(N-1):
                itr = 0
                x , y = strings[i], strings[i+1]
                n, m = len(x), len(y)
        
        
                while itr < min(n,m) and x[itr] == y[itr]:
                    itr+=1
                
                if itr == m and m < n:
                    return list("Impossible")
                if itr != min(n,m):
                    graph[x[itr]].append(y[itr])
                    indegree[y[itr]]+=1
        
        
            def top_sort(multi_source):
                queue = deque(multi_source)
                ans = []
        
                while queue:
                    x = queue.popleft()
                    ans.append(x)
                    for node in graph[x]:
                        indegree[node]-=1
                        if indegree[node]:
                            continue
                        queue.append(node)
        
        
                return ans
        
            multi_source = [node for node in indegree if indegree[node] == 0]
            ans = top_sort(multi_source)
            
            if len(ans) != K:
                return list("Impossible")
            else:
                return ans + list(alphabet - set(ans)) 
        
        
        return "".join(solve())
