# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from string import ascii_lowercase
from collections import defaultdict, deque

alphabet = set(ascii_lowercase)
indegree = {i: 0 for i in alphabet}

strings = []
t = int(input())
for _ in range(t):
    strings.append(input())


def solve():
    graph = defaultdict(list)

    for i in range(t-1):
        itr = 0
        n = len(strings[i])
        m = len(strings[i+1])




        while itr < min(n,m) and strings[i][itr] == strings[i+1][itr]:
            itr+=1
        
        if itr == m and m < n:
            return list("Impossible")
        if itr != min(n,m):
            graph[strings[i][itr]].append(strings[i+1][itr])
            indegree[strings[i+1][itr]]+=1


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

    multi_source = [node for node in indegree if not indegree[node]]
    ans = top_sort(multi_source)
    
    if len(ans) != 26:
        return list("Impossible")
    else:
        return ans + list(alphabet - set(ans)) 


print("".join(solve()))