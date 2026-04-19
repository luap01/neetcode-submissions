class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        for i in range(len(order) - 1):
            mp[order[i]] = i

        i = 0
        for w_idx in range(1, len(words)):
            while i < len(words[w_idx]) and i < len(words[w_idx-1]):
                if mp[words[w_idx][i]] < mp[words[w_idx-1][i]]:
                    return False
                elif mp[words[w_idx][i]] > mp[words[w_idx-1][i]]:
                    break
                i += 1
            
            if i >= len(words[w_idx]) and i < len(words[w_idx-1]):
                return False
            

        return True 
            