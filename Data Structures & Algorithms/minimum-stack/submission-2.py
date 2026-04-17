class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            # prev_val = self.min
            self.min = val
            # self.min_tracker[val] = prev_val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            # prev_val = self.min_tracker[val]
            # self.min = prev_val
            self.min = 2**31-1
            for i in self.stack:
                self.min = min(self.min, i)
            # del self.min_tracker[val]

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.min
