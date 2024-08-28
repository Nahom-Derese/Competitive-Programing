# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_ord = []
        for i in range(len(words)):
            word = words[i]
            word_ord = 0
            for char in word:
                x = ord(char) - ord("a")
                word_ord = word_ord | (1 << x)
            words_ord.append((word_ord, i))
            words[i] = len(word)

        words_ord.sort(reverse=True)
        max_ = 0
        for i in range(len(words_ord)):
            for j in range(i+1, len(words_ord)):
                if not (words_ord[i][0] & words_ord[j][0]):
                    x , y = words_ord[i][1], words_ord[j][1]
                    max_ = max(words[x]*words[y], max_)
        if max_:
            return max_
        return 0