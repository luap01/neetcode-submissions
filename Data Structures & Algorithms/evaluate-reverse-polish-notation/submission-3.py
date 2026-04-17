class Solution:
    def evalOp(self, l, r, op):
        if op == '+':
            return l + r
        if op == '-':
            return l - r
        if op == '*':
            return l * r
        if op == '/':
            return int(l / r)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] not in ('+', '-', '*', '/'):
                stack.append(int(tokens[i]))
            else:
                r = stack.pop()
                l = stack.pop()
                op = tokens[i]
                val = self.evalOp(l, r, op)
                stack.append(val)


        return stack.pop()
