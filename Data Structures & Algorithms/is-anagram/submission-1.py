class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for i in s:
            if i not in table:
                table[i] = 0
            table[i] += 1

        for i in t:
            if i not in table:
                return False
            if i in table:
                table[i] -= 1
            if table[i] < 0:
                return False

        for i in table:
            if table[i] != 0:
                return False
        return True