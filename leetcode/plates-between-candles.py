class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        indexes = [i for i in range(len(s)) if s[i] == "|"]
        ans = []
        for start, end in queries:
            l = bisect_left(indexes, start)
            r = bisect_right(indexes, end)

            if r == l:
                ans.append(0)
                continue
            ans.append((indexes[r-1] - indexes[l]) - (r - l - 1))

        return ans