class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid),len(grid[0])
        queue = deque()
        visited = set ()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))
        def addCell(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r,c))
            queue.append((r,c))
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            distance += 1
        return

