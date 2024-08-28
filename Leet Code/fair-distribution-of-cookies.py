class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = float('inf')

        if k == len(cookies):
            return max(cookies)

        def backtrack(current, index):
            nonlocal ans
            # print(current)
            if index >= len(cookies):
                ans = min(ans, max(current))
                return
            
            for i in range(k):
                current[i]+=cookies[index]
                backtrack(current, index+1)
                current[i]-=cookies[index]

        backtrack([0 for i in range(k)], 0)

        return ans
