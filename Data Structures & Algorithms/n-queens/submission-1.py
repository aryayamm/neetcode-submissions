class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        row = [0]*n
        col = [0]*n
        d1 = [0]*(n*2) #sum
        d2 = [0]*(n*2) #dif
        def solve(r, arr):
            if r == n:
                res = [] 
                for i in arr:
                    temp = ""
                    for j in i:
                        if j == 0:
                            temp += "."
                        else:
                            temp += "Q"
                    res.append(temp)
                ans.append(res)
                return

            if row[r] == 1:
                solve(r+1)

            for c in range(n):
                if col[c] != 1 and d1[r+c] != 1 and d2[r-c+n] != 1:
                    row[r] = 1
                    col[c] = 1
                    d1[r+c] = 1
                    d2[r-c+n] = 1
                    arr[r][c] = 1
                    solve(r+1, arr)
                    row[r] = 0
                    col[c] = 0
                    d1[r+c] = 0
                    d2[r-c+n] = 0
                    arr[r][c] = 0

        plain = [[0] * n for i in range(n)]
        solve(0, plain)
        return ans
            