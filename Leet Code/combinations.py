class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1, n+1)]
        def backtrack(current, candidates):
            if len(current) == k:
                ans.append(current[:])
                return 
            
            for i in range(len(candidates)):
                current.append(candidates[i])
                backtrack(current, candidates[i+1:])
                current.pop()

        backtrack([], nums[:])
        return ans