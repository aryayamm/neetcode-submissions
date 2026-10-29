class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        num = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        def solve(i,s):
            if i == len(digits):
                if s != "":
                    ans.append(s)
                return
            for n in num[int(digits[i])]:
                solve(i+1, s + n)
        solve(0,"")
        return ans