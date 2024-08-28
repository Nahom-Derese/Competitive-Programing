# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        iterator = self.root
        for char in word:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                iterator.children[loc] = TrieNode()
            
            iterator = iterator.children[loc]
            
        iterator.is_end = True 

    def search(self, word: str) -> bool:
        

        def find(word, iterator):
            
            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    for j in range(26):
                        if iterator.children[j] and find(word[i+1:], iterator.children[j]):
                            return True
                    return False
                

                loc = ord(char) - ord('a')
                if not iterator.children[loc]:
                    return False
                
                iterator = iterator.children[loc]

            return iterator.is_end

        return find(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)