class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        visited = set()
        def dfs(i, j, curr_area):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            if (i, j) in visited:
                return 0
    
            if grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            inc = 1
            u = dfs(i+1, j, curr_area)
            d = dfs(i-1, j, curr_area)
            r = dfs(i, j+1, curr_area)
            l = dfs(i, j-1, curr_area)
            curr_area = inc+u+d+l+r
            return curr_area
        

        nodes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j, 0), max_area)

        return max_area