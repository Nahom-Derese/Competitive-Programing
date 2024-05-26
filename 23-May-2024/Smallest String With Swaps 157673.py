# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size+1)}
        self.size = {i:1 for i in range(size+1)}


    def find(self, query):
        if self.parent[query] == query:
            return query

        self.parent[query] = self.find(self.parent[query])
        return self.parent[query]



    def union(self, query1, query2):
        parent1 = self.find(query1)
        parent2 = self.find(query2)

        if parent1 == parent2:
            return

        size1 = self.size[parent1]
        size2 = self.size[parent2]
        
        if size1 > size2:
            self.parent[parent2] = parent1
            self.size[parent1]+=size2
        else:
            self.parent[parent1] = parent2
            self.size[parent2]+=size1



class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        UF = UnionFind(len(s))
        
        for a, b in pairs:
            UF.union(a, b)
        
        mapp = defaultdict(list)

        for i in range(len(s)):
            heappush(mapp[UF.find(i)], s[i])
        
        ans = ""
        for i in range(len(s)):
            ans+=heappop(mapp[UF.find(i)])
        
        return ans