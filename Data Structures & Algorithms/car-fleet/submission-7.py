import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedFleet = sorted(zip(position, speed), reverse=True)

        # 7, 4, 1, 0
        # 1, 2, 9, 1
        # 3, 3, 1, 10
        # 

        # 8, 6
        # 2, 3
        # 1, 2

        # 4, 2, 0
        # 1, 3, 2
        # 6, 3, 5
        stack = []
        for p, s in sortedFleet:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
