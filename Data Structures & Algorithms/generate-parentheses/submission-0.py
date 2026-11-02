class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(a,b,s):
            # print(s)
            nonlocal n
            if a == 0:
                s += b * ")"
                # print(f"done {s}")
                ans.append(s)
                return

            solve(a-1, b, s+"(")

            if b - a != 0:
                solve(a, b -1, s+")")
            return
        solve(n-1,n, "(")

        return ans