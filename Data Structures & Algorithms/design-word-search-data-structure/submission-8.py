class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def dfs(self, node, i, word):
        if i < 0 or i >= len(word):
            return node.endOfWord

        c = word[i]
        idx = ord(c) - ord("a")
        if c == ".":
            res = []
            for k in range(26):
                if node.children[k] is not None:
                    res.append((self.dfs(node.children[k], i+1, word)))
            for out in res:
                if out == True:
                    return True
            return False
        elif node.children[idx] == None:
            return False
        else:
            return self.dfs(node.children[idx], i+1, word)
            

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)