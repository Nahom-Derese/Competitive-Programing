class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = -k
        r = 0

        current=sum(cardPoints[-k:])
        ans = current
        while r < k:
            current+=cardPoints[r]
            current-=cardPoints[l]

            ans = max(current, ans)
            r+=1
            l+=1

        return ans