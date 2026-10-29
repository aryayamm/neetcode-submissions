class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {"{":"}", "[":"]", "(":")"}
        for i in range(len(s)):
            if s[i] in table:
                stack.append(s[i])
                continue
            if not stack:
                return False
            top=stack.pop()
            if s[i]==')'and top!='(':
                return False
            if s[i]==']'and top!='[':
                return False
            if s[i]=='}'and top!='{':
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        