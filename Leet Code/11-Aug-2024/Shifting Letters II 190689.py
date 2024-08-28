# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_sum = [0] * (len(s)+1)
        mapp = ascii_lowercase

        for a, b, c in shifts:
            if c:
                pre_sum[a] += 1
                pre_sum[b+1] -= 1
            else:
                pre_sum[a] -= 1
                pre_sum[b+1] += 1
        
        pre_sum = list(accumulate(pre_sum))
        ans = ""
        for i in range(len(s)):
            ans += mapp[((ord(s[i]) - 97) + pre_sum[i]) % 26]
        
        return ans