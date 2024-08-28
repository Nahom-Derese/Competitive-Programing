class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        x = Counter(answers)

        ans = 0
        for i in x:
            ans+=x[i]
            o=i+1
            if x[i] % o != 0:
                ans+= o - (x[i] % o)
        
        return ans