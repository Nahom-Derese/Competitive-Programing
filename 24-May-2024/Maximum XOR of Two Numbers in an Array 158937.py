# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        iterator = self.root
        for char in word:
            if not iterator.children[int(char)]:
                iterator.children[int(char)] = TrieNode()
            
            iterator = iterator.children[int(char)]
            
        iterator.is_end = True 

    def search(self, word: str) -> None:
        itr = self.root

        res = ""
        for char in word:
            if not itr:
                return int(res, 2)
            if itr.children[~int(char)]:
                res+="1"
                itr = itr.children[~int(char)]
            else:
                res+="0"
                itr = itr.children[int(char)]
            
        
        return int(res, 2)

    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        for num in nums:
            y = bin(num)[2:]
            y = y.zfill(32)
            trie.insert(y)
        
        ans = 0
        for num in nums:
            y = bin(num)[2:]
            y = y.zfill(32)
            ans = max(trie.search(y), ans)

        return ans