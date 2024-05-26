class TrieNode:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.left = None
        self.right = None

    def has_options(self):
        return self.children.count(None) > 0




class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, n:int) -> None:
        dummy = self.root

        def rec_insert(node: TrieNode, length: int):

            if length == 1:
                if node.left == None:
                    node.left = TrieNode(True)
                    return "0"
                elif node.right == None:
                    node.right = TrieNode(True)
                    
                    return "1"
                return False

            
            if not node.left:
                node.left = TrieNode()
            
            if not node.left.is_end:
                val = rec_insert(node.left, length-1)
                if val:
                    return "0" + val



            if not node.right:
                node.right = TrieNode()
            
            if not node.right.is_end:
                val = rec_insert(node.right, length-1)
                if val:
                    return "1" + val

            return False

        return rec_insert(dummy, n)

    def search(self, word:str) -> None:
        dummy = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if dummy.children[pos] == None:
                return False

            dummy = dummy.children[pos]

        return dummy.is_end


def solve(lens):
    trie = Trie()
    res = []
    for length in lens:
        x = trie.insert(length)
        if x == False:
            return False
        res.append(x)
    return res


n = int(input())
lens = [int(i) for i in input().split()]

answer = solve(lens)

if answer:
    print("YES")
    for ans in answer:
        print(ans)
else:
    print("NO")