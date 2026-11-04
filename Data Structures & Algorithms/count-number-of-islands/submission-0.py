class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        r = len(grid)
        c = len(grid[0])
        def solve(row,col):
            nonlocal r,c,grid
            if not(0 <= row < r and 0 <= col < c):
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            solve(row+1,col)
            solve(row-1,col)
            solve(row,col+1)
            solve(row,col-1)

            return
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    solve(i,j)
                    island += 1

        return island
        
            