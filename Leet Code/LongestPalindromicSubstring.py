class Solution:
    def longestPalindrome(self, s: str):
        length = len(s)
        answer = []
        for i in [0,1]:
            ans = ""
            left_ptr = 0
            right_ptr = length-1
            clck = i
            while left_ptr < right_ptr:
                if s[left_ptr] == s[right_ptr]:
                    ans+=s[left_ptr]
                else:
                    ans=""
                if clck%2==0:
                    right_ptr-=1
                else:
                    left_ptr+=1
                clck+=1
            answer.append(ans)
            

        return answer 

print(Solution.longestPalindrome(Solution, "bab"))
print(Solution.longestPalindrome(Solution, "bab"))