class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        def save(x,y):
            if not (0 <= x < r and 0 <= y < c):
                return
            if board[x][y] == "X":
                return
            if board[x][y] == "S":
                return
            board[x][y] = "S"
            save(x-1,y)
            save(x+1,y)
            save(x,y+1)
            save(x,y-1)
            return        

        for i in range(r):
            save(i,0)
            save(i,c-1)

        for i in range(c):
            save(0,i)
            save(r-1,i)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j]="O"


        