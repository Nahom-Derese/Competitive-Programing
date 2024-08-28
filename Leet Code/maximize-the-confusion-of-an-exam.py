class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = r = 0
        T = F = 0
        ans = 0
        while r < len(answerKey):
            T += answerKey[r] == 'T'
            F += answerKey[r] == 'F'

            while min(T,F) > k:
                T -= answerKey[l] == 'T'
                F -= answerKey[l] == 'F'
                l+=1

            ans = max(ans,r-l+1)
            
            r+=1
        return ans