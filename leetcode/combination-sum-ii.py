class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        
        candidates = list(filter(lambda x: x <= target, candidates))

        candidates.sort()

        def backtrack(current, summ, idx):
            
            if summ == target:
                ans.add(tuple(current[:]))
                return

            seen = set()
            for i in range(idx, len(candidates)):
                if candidates[i] in seen:
                    continue
                if summ + candidates[i] <= target:
                    summ+=candidates[i]
                    
                    current.append(candidates[i])
                    
                    backtrack(current, summ, i+1)
                    
                    n = current.pop()
                    seen.add(n)
                    summ-=n

        backtrack([], 0, 0)

        return ans