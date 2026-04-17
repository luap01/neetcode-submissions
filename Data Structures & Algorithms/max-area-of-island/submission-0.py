class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        visited = set()
        def dfs(i, j, curr, curr_area):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            if (i, j) in curr:
                return 0
    
            if grid[i][j] == 0:
                return 0
            
            inc = 1 if grid[i][j] == 1 else 0
            curr.add((i,j))
            u = dfs(i+1, j, curr, curr_area)
            d = dfs(i-1, j, curr, curr_area)
            r = dfs(i, j+1, curr, curr_area)
            l = dfs(i, j-1, curr, curr_area)
            curr_area = max(curr_area, inc+u+d+l+r)
            return curr_area
        

        nodes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    nodes.append((i,j))
        
        for (i, j) in nodes:
            max_area = max(dfs(i, j, set(), 0), max_area)

        return max_area