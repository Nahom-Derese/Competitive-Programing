# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        candidates = []

        for i in range(len(s)):
            if s[i].isalpha():
                candidates.append(i)

        ans = []
        for i in range((1 << (len(candidates)))):
            state = list(s)
            for itr in candidates:
                if (i & 1):
                    state[itr] = state[itr].swapcase()
                i >>= 1
            ans.append("".join(state))
       
        return ans