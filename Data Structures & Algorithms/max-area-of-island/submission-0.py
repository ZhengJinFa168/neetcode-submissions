class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        ROW,COL = len(grid),len(grid[0])
        def dfs(r,c,area):
            if r < 0 or c < 0 or r >=ROW or c >= COL or (r,c) in visited or grid[r][c] == 0:
                return area
            visited.add((r,c))
            area += 1
            return area + dfs(r+1,c,0) + dfs(r-1,c,0) + dfs(r,c+1,0) + dfs(r,c-1,0)
        
        for i in range(ROW):
            for j in range(COL):
                maxArea = max(maxArea,dfs(i,j,0))

        return maxArea