class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c, 0))
        
        dirs = [(1,0), (0,1), (-1,0),(0,-1)]

        while q:
            r, c, t = q.popleft()
            minutes = max(minutes, t)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    q.append((nr,nc, t + 1))

        for r in grid:
            if 1 in r:
                return -1
        return minutes




        