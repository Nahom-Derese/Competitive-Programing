from functools import lru_cache
from functools import cache

MOD = 1000000007

class Solution:
    def knightDialer(self, n: int) -> int:
        neighbours = {
            0: [6,4],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
        }

        if n == 1:
            return 10

        memo = {}
        
        @cache
        def DFS(length, node):    
            if length == n:
                return 1
            
            total = 0
            for i in neighbours[node]:
                total += DFS(length+1, i) % MOD


            return total % MOD

        answer = 0

        for i in neighbours:
            answer+= DFS(1,i)
            answer%= MOD

        return answer % MOD

            
print(Solution().knightDialer(3131))