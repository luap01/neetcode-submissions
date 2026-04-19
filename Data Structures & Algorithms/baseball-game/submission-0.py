class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                v2 = stack.pop()
                v1 = stack.pop()
                r = v1 + v2
                stack.append(v1)
                stack.append(v2)
                stack.append(r)
            elif op == 'D':
                v = stack.pop()
                stack.append(v)
                stack.append(v*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        res = 0
        while stack:
            res += stack.pop()
        
        return res