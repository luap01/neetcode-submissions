class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(0, len(heights)):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                while stack and stack[-1][1] > heights[i]:
                    j, h = stack.pop()
                    width = i - j
                    area = h * width
                    max_area = max(max_area, area)
                    start = j
                stack.append((start, heights[i]))
        
        stack_length = len(heights)
        while stack:
            j, h = stack.pop()
            width = stack_length - j       
            area = h * width
            max_area = max(max_area, area)

        return max_area
