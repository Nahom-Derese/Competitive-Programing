# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        iterator = self.root
        for char in word:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                iterator.children[loc] = TrieNode()
            
            iterator = iterator.children[loc]
            
        iterator.is_end = True 

    def search(self, word: str) -> bool:
        iterator = self.root
        for char in word:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                return False
            
            iterator = iterator.children[loc]

        return iterator.is_end

    def startsWith(self, prefix: str) -> bool:
        iterator = self.root
        for char in prefix:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                return False
            
            iterator = iterator.children[loc]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)