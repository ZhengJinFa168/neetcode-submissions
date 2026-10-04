class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW,COL = len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c <0 or r >= ROW or c >= COL or (r,c) in visited or grid[r][c]=="0":
                return
            
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        count = 0
        for i in range(ROW):
            for j in range(COL):
                if not ((i,j) in visited or grid[i][j]=="0"):
                    count += 1
                    dfs(i,j)
        return count
            

