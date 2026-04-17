class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        s = s.replace(" ", "").lower()
        for c in s:
            if c.isalnum():
                res += c
        return res == res[::-1]