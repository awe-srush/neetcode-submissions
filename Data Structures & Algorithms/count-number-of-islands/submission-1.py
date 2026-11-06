class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr,nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands        
        