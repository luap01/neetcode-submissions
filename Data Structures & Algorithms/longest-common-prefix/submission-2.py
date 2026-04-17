class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        for s in strs:
            curr = root
            for c in s:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
        
        curr = root
        notFound = True
        res = ""
        while notFound:
            children = list(curr.children.keys())
            if curr.endOfWord or len(children) > 1 or len(children) == 0:
                return res
            curr = curr.children[children[0]]
            res += children[0]

        return ""
        