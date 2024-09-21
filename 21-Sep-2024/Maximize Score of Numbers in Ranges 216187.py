# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        ans = 0
        

        # brute force is just trying all possible case
        # def backtrack(i, curr):
        #     if i == len(start):
        #         curr.sort()
        #         curr.append(curr[0])
                
        #         res = float("inf")
        #         for j in range(1, len(curr)):
        #             res = min(abs(curr[j] - curr[j-1]), res)
                
        #         return res

        #     res = 0
        #     for j in range(d+1):
        #         curr.append(start[i] + j)
        #         res = max(res, backtrack(i+1, curr[:]))
        #         curr.pop()
                
        #     return res

        # return backtrack(0, [])


        # using binary search
        # 6        0          3
        # 6 7 8    0 1 2      3 4 5
        
        def helper(target):
            candidate = start[0]
            
            for i in range(1, len(start)):
                candidate += target
                candidate = max(candidate, start[i])

                if candidate > start[i] + d:
                    return False

            return True

        l =  1
        r = start[-1] - start[0] + d

        while l <= r:
            m = l + (r - l) // 2

            if helper(m):
                l = m + 1
            else:
                r = m - 1
            
        return l - 1
        
