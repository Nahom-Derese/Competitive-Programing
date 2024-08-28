class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        l = r = 0

        count = set()
        ans = float("inf")
        while r < len(cards):
            if cards[r] in count:
                
                while cards[r] in count:
                    count.remove(cards[l])
                    l+=1

                ans = min(ans, r-l+2)

            count.add(cards[r])
            r+=1
        if ans == float("inf"):
            return -1
        return ans