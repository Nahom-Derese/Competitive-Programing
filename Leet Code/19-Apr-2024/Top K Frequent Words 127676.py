# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        ans = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        return ans[:k]