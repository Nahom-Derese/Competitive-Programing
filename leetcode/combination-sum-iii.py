class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = set()

        def backtrack(candidates, current, summ):
            print(current)
            if len(current) == k and summ == n:
                ans.add(tuple(sorted(current[:]))) 
                return
            
            for i in range(len(candidates)):
                if len(current) < min(n,k) and candidates[i] <= n:
                    current.append(candidates[i])
                    backtrack(candidates[i+1:], current[:], summ+candidates[i])
                    current.pop()

        backtrack([1,2,3,4,5,6,7,8,9], [], 0)

        # print(ans)

        return ans