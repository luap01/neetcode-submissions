class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack and stack[-1] > 0 and asteroid < 0:
                while stack and stack[-1] > 0 and asteroid + stack[-1] < 0:
                    stack.pop()
                
                if stack:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                    elif stack[-1] < 0:
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        
        return stack