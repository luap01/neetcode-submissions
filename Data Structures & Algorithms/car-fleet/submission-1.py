class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), reverse=True)

        # 10, 2, 2
        # 8, 6, 1 


        stack = []
        for pos, speed in sorted_cars:
            steps = (target - pos) / speed
            if stack and steps > stack[-1]:
                stack.append(steps)
            elif not stack:
                stack.append(steps)

        return len(stack)