class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        y = ceil(target/min(candidates))
        def comb(current, c):
            if len(current) > y or sum(current) > target:
                return
            if sum(current) == target:
                ans.add(tuple(sorted(current[:])))
                return
        
            for i in range(len(c)):
                current.append(c[i])
                comb(current, c[:])
                current.pop()
            
        comb([], candidates[:])

        return ans