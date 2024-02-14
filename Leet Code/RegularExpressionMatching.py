import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        patter = re.compile(p)
        return(bool(patter.fullmatch(s)))

Solution.isMatch(Solution, 'aa', 'a')