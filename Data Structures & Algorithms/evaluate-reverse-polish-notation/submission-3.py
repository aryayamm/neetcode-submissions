class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        for i in tokens:
            if i.lstrip('-').isdigit() :
                num.append(int(i))
            else:
                a = int(num.pop())
                b = int(num.pop())
                if i == "+": num.append(b+a)
                elif i == "-": num.append(b-a)
                elif i == "*": num.append(b*a)
                elif i == "/": num.append(int(b/a))
        return num[0]
                    