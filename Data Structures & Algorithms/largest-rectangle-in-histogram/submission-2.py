class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # 4, 0, 0
        # 2, 2, 1
        # 2, 1, 2
        # 7, 0, 0
        # 1, 1, 4
        # 7, 0, 0 
 
        max_area = 0
        for i in range(0, len(heights)):
            height = heights[i]
            width = 1
            # left
            for j in range(i-1, -1, -1):
                if heights[j] >= height:
                    width += 1
                else:
                    break
            # right
            for j in range(i+1, len(heights)):
                if heights[j] >= height:
                    width += 1
                else:
                    break

            if width*height > max_area:
                max_area = width*height
        
        return max_area
