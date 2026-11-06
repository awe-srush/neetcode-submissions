class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        area = 0

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == 0):
                return
            visited.add((r,c))
            nonlocal area
            area += 1
            dfs(r, c - 1)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                if area > max_area:
                    max_area = area
                area = 0
        return max_area


        
        