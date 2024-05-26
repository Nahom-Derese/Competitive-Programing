class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

    def empty(self):
        return self.children.count(None) == 26


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.lengths = []

    def insert(self, word:str) -> None:
        dummy = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if dummy.children[pos] == None:
                dummy.children[pos] = TrieNode()

            dummy = dummy.children[pos]

        dummy.is_end = True
        self.lengths.append(len(word))
    
    def calc(self, word:str) -> None:
        dummy = self.root
        for char in word:
            
            pos = ord(char) - ord('a')
            if dummy.children[pos] == None:
                return 

            dummy = dummy.children[pos]

        dummy.is_end = True
        self.lengths.append(len(word))

    def search(self, word:str) -> None:
        dummy = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if dummy.children[pos] == None:
                return False

            dummy = dummy.children[pos]

        return dummy.is_end


trie = Trie()

def solve(val):
    trie.insert(val[::-1])
    return trie.calc(val)


ans = 0
for _ in range(int(input())):
    val = input()
    ans+=solve(val)

print(ans)