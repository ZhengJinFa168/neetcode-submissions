class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        ROW, COLS = len(grid),len(grid[0])
        self.numFreshFruits = 0
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    self.numFreshFruits += 1
        
        if self.numFreshFruits == 0:
            return 0
        
        def addCell(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                self.numFreshFruits -= 1
            q.append((r,c))
            visited.add((r,c))
        
        time = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            time += 1
        if self.numFreshFruits > 0:
            return -1
        return time
                