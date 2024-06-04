# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        itr = self.root

        for i in range(len(word)):
            char = word[i]
            idx = ord(char) - ord("a")

            if not itr.children[idx]:
                if i == len(word)-1:
                    itr.is_end = False
                    itr.children[idx] = TrieNode()
                    itr.children[idx].is_end = True
                return
            
            itr = itr.children[idx]
        

    def search(self, word):
        itr = self.root

        for char in word:
            idx = ord(char) - ord("a")

            if not itr.children[idx]:
                return False
            
            itr = itr.children[idx]
        
        return itr.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for word in sorted(words):
            trie.insert(word)
        
        ans = []
        for word in sorted(words, key=len):
            if trie.search(word):
                ans.append(word)

        ans.sort(key= lambda x: (-len(x), x))
        
        if ans:
            return ans[0]
        return ""