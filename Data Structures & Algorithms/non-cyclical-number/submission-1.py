class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()
        s = str(n)

        while True:
            cur = 0
            for i in s:
                cur += int(i)**2
            if cur not in table:
                table.add(cur)
            else:
                return False
            if cur == 1: return True
            s = str(cur)