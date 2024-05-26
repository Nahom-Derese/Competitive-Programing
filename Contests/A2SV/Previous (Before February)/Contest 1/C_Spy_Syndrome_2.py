class TrieNode:
	def __init__(self):
		self.is_end = False
		self.children = [ None for _ in range(26) ]

	def empty(self):
		return self.children.count(None) == 26


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word:str) -> None:
		dummy = self.root
		for char in word:
			pos = ord(char) - ord('a')
			if dummy.children[pos] == None:
				dummy.children[pos] = TrieNode()

			dummy = dummy.children[pos]

		dummy.is_end = True

	def search(self, word:str) -> None:
		dummy = self.root
		for char in word:
			pos = ord(char) - ord('a')
			if dummy.children[pos] == None:
				return False

			dummy = dummy.children[pos]

		return dummy.is_end

	def delete(self, word: str) -> None:
		if not self.search(word):
			return

		def recurse_delete(node, idx):
			if idx == len(word):
				if node.empty():
					return None
				node.is_end = False
				return node

			pos = ord(word[idx]) - ord('a')
			node.children[pos] = recurse_delete(node.children[pos], idx+1)
			if not node.is_end and node.empty():
				return None
			return node

		recurse_delete(self.root, 0)


n = int(input())
s = input()
word_len = int(input())

trie = Trie()

for _ in range(word_len):
    word = input()
    trie.insert(word)
