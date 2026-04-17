class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in [')', '}', ']']:
                if len(stack) > 0:
                    val = stack.pop()
                    if c == ')' and val != '(' or c == '}' and val != '{' or c == ']' and val != '[':
                        return False
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0