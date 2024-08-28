class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = dict(Counter(s))
        ans = 0
        flag = True
        for i, j in x.items():
            if (not j%2):
                ans+=j
            else:
                if flag:
                    ans+=j
                    flag=False
                else:
                    ans+=j-1

        if len(set(s)) == 1:
            return len(s)
        return ans
