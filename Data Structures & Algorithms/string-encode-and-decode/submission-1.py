class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            size = len(s)
            encoded_s += str(size) 
            encoded_s += "#"
            encoded_s += s
        return encoded_s 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            readLen = True
            size = int(s[i])
            while readLen:
                i += 1
                if s[i] != "#":
                    size = size * 10 + int(s[i])
                else:
                    readLen = False
                    i += 1
        
            strs.append(s[i:i+size])
            i += size

        return strs
            

