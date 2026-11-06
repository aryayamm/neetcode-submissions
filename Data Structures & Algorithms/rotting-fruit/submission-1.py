class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = 0
        time = -1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i in d:
                    a = x + i[0]
                    b = y + i[1]
                    if not (0 <= a < r and 0 <= b < c):
                        continue
                    if grid[a][b] != 1:
                        continue
                    grid[a][b] = 0
                    q.append((a, b))
            time += 1

        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return max(time, 0)