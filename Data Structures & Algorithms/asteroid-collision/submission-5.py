class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # ast neg stack top pos
            if stack and stack[-1] > 0 and asteroid < 0:
                # while ast stronger than top -> destroy top 
                while stack and stack[-1] > 0 and asteroid + stack[-1] < 0:
                    stack.pop()
                # nothing left append ast or top neg as well
                if not stack or stack and stack[-1] < 0:
                    stack.append(asteroid)
                # ast same as top -> destroy both
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                # ast weaker -> continue
            else:
                # both same direction -> append
                # top neg and ast pos -> append
                stack.append(asteroid)
        
        return stack