# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}
        self.summ = {i:0 for i in range(size)}
        self.maxx = 0


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
            self.summ[parent1]+=self.summ[parent2]
            self.maxx = max(self.maxx, self.summ[parent1])
        else:
            self.parent[parent1] = parent2
            self.size[parent2]+=size1
            self.summ[parent2]+=self.summ[parent1]
            self.maxx = max(self.maxx, self.summ[parent2])



class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        visited = set()

        DSU = UnionFind(len(nums))
        ans = deque([0])
        for i in removeQueries[::-1]:
            visited.add(i)
            DSU.summ[i] = nums[i]
            DSU.maxx = max(DSU.maxx, nums[i])
            if i-1 > -1 and i-1 in visited:
                DSU.union(i, i-1)
            if i+1 < len(nums) and i+1 in visited:
                DSU.union(i, i+1)
            ans.appendleft(DSU.maxx)
        ans.popleft()
        return ans