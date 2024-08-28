# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

class TrieNode:
    def __init__(self):
     self.child= {}
     self.cnt = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            ind=ord(c)-ord("a")

            if ind  not in cur.child:
                cur.child[ind]=TrieNode()
            
            cur=cur.child[ind]
            cur.cnt += 1
    
    def search(self, word: str) -> int:
     
        itr=self.root
        tot = 0
        for c in word:
            ind=ord(c)-ord("a")
            if ind not in itr.child:
                return tot
            
            itr=itr.child[ind]
            tot += itr.cnt * 2

        return tot
     

trie = Trie()
strings = []

for _ in range(int(input())):
    val = input()
    strings.append(val)
    trie.insert(val)


ans = sum([len(string)*2*len(strings) for string in strings])
for val in strings:
    ans-=trie.search(val[::-1])

print(ans)