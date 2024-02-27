class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ans = r = k
        l = 0
        freq = Counter(blocks[:k])
        ans = freq['W']
        while r < len(blocks):
            freq[blocks[r]]+=1
            freq[blocks[l]]-=1

            ans = min(ans, freq['W'])
            
            r+=1
            l+=1

        return ans