class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        precedence = {'/':4, '*':4, '+': 2, '-': 2}
        if not any(element in s for element in precedence.keys()):
            return int(s)

        stack = []
        postfix = []
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num*=10
                num+=int(s[i])
            else:
                postfix.append(str(num))
                num = 0
                if len(stack)==0:
                    stack.append(s[i])
                else:
                    while len(stack)!=0 and (precedence[s[i]]<=precedence[stack[-1]]):
                        postfix.append(stack.pop())
                    stack.append(s[i])

        if num!=0 or s[-1].isdigit():
            postfix.append(str(num))

        while(len(stack)!=0):
            postfix.append(stack.pop())
        
        operands = []
        for i in postfix:
            if i.isnumeric():
                operands.append(int(i))
            else:
                n2 = operands.pop()
                n1 = operands.pop()
                if i=='+':
                    res = n1 + n2
                elif i=='-':
                    res = n1 - n2
                elif i=='*':
                    res = n1*n2
                elif i=='/':
                    res = int(n1/n2)
                operands.append(res)
        
        return operands[0]

sol = Solution()
print(sol.calculate('21+1+1'))