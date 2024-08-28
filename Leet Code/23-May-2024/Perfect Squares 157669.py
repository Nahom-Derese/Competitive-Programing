# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]
        # perfect_squares = [i*i for i in range(1,101)]
        # if n in perfect_squares:
        #     return 1
        # i = 0
        # while perfect_squares[i] < n:
        #     i+=1
        # ans=float('inf')
        
        # @cache
        # def recur(node,rem,hops):
        #     if rem == 0:
        #         return hops-1
            
        #     if perfect_squares[node] == 1:
        #         return hops+rem-1
            
        #     ans = float('inf')
        #     for i in range(node+1, 0, -1):
        #         new_rem = rem-perfect_squares[node]
        #         if new_rem > -1:
        #             ans = min(ans,recur(i, new_rem, hops+1))
            
        #     return ans

        # ans = float('inf')
        # for j in range(i//2,i):
        #     ans = min(recur(j, n, 1), ans)
        
        # return ans