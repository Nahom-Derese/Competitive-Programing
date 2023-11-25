class Solution:
    def romanToInt(self, s: str) -> int:
        x = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
            }
        
        ans = 0

        for i in range(len(s)):
            left_ptr = i - 1
            right_ptr = i + 1
            if left_ptr >= 0 and x[s[i]] > x[s[left_ptr]]:
                ans += x[s[i]] - 2 * x[s[left_ptr]]
                continue
            else:
                ans += x[s[i]]

        return ans


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))