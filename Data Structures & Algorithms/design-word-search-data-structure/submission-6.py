class WordDictionary:
    def found(self, search, lst, word):   
        if search in lst:
            for search_word in lst[search]:
                compare_word = search_word
                if len(compare_word) == len(word):
                    found = True
                    for i in range(len(compare_word)):
                        if word[i] != "." and word[i] != compare_word[i]:
                            found = False
                            break
                else:
                    continue
                if found:
                    return True
        return False
    
    def __init__(self):
        self.words = defaultdict(int)
        self.prefix = defaultdict(list)
        self.postfix = defaultdict(list)
        for i in range(97, 123):
            self.prefix[""].append(chr(i))
            self.postfix[""].append(chr(i))

    def addWord(self, word: str) -> None:
        self.words[word] = 1
        prefix = ""
        postfix = ""
        for i in range(len(word)):
            prefix += word[i]
            postfix += word[-(i+1)]
            self.prefix[prefix].append(word)
            self.postfix[postfix[::-1]].append(word)

    def search(self, word: str) -> bool:
        if "." in word:
            search_parts = word.split(".")
            if len(word) == 1 and "." in word or len(word) == 2 and ".." in word:
                for w in self.words.keys():
                    if len(w) == len(word):
                        return True
                return False

            for search in search_parts:
                pre_found = self.found(search, self.prefix, word)
                post_found = self.found(search, self.postfix, word)
                if pre_found or post_found:
                    return True
            return False
        else:
            return word in self.words
