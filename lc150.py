class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if i == '+':
                    res = n1+n2
                elif i == '-':
                    res = n1 - n2
                elif i == '*':
                    res = n1*n2
                elif i == '/':
                    res = int(n1/n2)
                stack.append(res)
        
        return stack[0]

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))