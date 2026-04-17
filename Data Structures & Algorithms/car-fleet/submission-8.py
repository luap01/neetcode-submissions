class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedFleet = sorted(zip(position, speed), reverse=True)

        stack = []
        for p, s in sortedFleet:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
