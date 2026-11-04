class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        r = len(grid)
        c = len(grid[0])
        island = 0
        visit = [[False]*c for i in range(r)]
        cur = 0
        def solve(row,col,n):
            nonlocal r,c,directions,grid,cur
            if not(0 <= row < r and 0 <= col < c):
                return
            if grid[row][col] == 0:
                return
            grid[row][col] = 0
            for i in directions:
                solve(row + i[0], col + i[1], n+1)
            cur += 1
            return 

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    solve(i,j,1)
                    island = max(cur,island)
                    # for a in grid:
                    #     print(a)
                    # for a in range(c):
                    #     print("-", end="")
                    # print(island)
                cur = 0
        return island