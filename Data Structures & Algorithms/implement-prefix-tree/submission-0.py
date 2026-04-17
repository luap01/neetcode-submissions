class PrefixTree:

    def __init__(self):
        self.search_table = {}
        self.prefix_table = {}

    def insert(self, word: str) -> None:
        self.search_table[word] = 1
        prefix = ""
        for c in word:
            prefix += c
            self.prefix_table[prefix] = 1

    def search(self, word: str) -> bool:
        return word in self.search_table

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_table
        