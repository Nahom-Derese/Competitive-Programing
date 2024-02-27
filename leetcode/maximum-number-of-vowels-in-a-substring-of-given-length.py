class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        r = k
        l = ans = currentFreq = 0
        
        for i in s[:r]:
            if i in vowels:
                currentFreq+=1
        
        ans = currentFreq

        while r < len(s):
            print(currentFreq)
            if s[r] in vowels:
                currentFreq+=1

            if s[l] in vowels:
                currentFreq-=1

            ans = max(ans, currentFreq)

            r+=1
            l+=1
        
        return ans