# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
                itr.children[idx] = TrieNode()
                    
            itr = itr.children[idx]
        
        itr.is_end = True

    def search(self, word):
        itr = self.root
        count = 0
        for char in word:
            idx = ord(char) - ord("a")
            
            if itr.is_end:
                return word[:count]
            
            
            if not itr.children[idx]:
                return False
            
            
            count+=1
            itr = itr.children[idx]
        
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        
        ans = ""
        for word in sentence.split():
            root = trie.search(word)

            if root == False:
                ans+= word + " "
                continue
                
            ans += root + " "
        
        return ans.strip()