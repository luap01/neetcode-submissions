class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))
            encoded_str += "#"
            encoded_str += word
            encoded_str += "#"
        return encoded_str
    # 444#neet#
    # 4#code#
    # 4#love#
    # 4#4444#


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = int(s[i])
            i += 1
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            res.append(s[i:i+length])
            i += length
            i += 1
        return res
