class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        a = len(board)
        b = len(board[0])
        ans = False
        check = [[0] * b for _ in range(a)]
        print(check)
        def solve(r,c,n):
            nonlocal a,b,word,board, ans
            if n == len(word):
                ans = True
                return
            if 0 <= r + 1 < a:
                if board[r+1][c] == word[n] and check[r+1][c] == 0:
                    check[r+1][c] = 1
                    solve(r+1,c,n+1)
                    check[r+1][c] = 0

            if 0 <= r - 1 < a:
                if board[r-1][c] == word[n] and check[r-1][c] == 0:
                    check[r-1][c] = 1
                    solve(r-1,c,n+1)
                    check[r-1][c] = 0

            if 0 <= c + 1 < b:
                if board[r][c+1] == word[n] and check[r][c+1] == 0:
                    check[r][c+1] = 1
                    solve(r,c+1,n+1)
                    check[r][c+1] = 0

            if 0 <= c - 1 < b:
                if board[r][c-1] == word[n] and check[r][c-1] == 0:
                    check[r][c-1] = 1
                    solve(r,c-1,n+1)
                    check[r][c-1] = 0
            return ans

        for i in range(a):
            for j in range(b):
                if board[i][j] == word[0]:
                    check[i][j] = 1
                    solve(i,j,1)
                    check[i][j] = 0
                    if ans == True:
                        return True
        
        return False