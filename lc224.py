class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        
        stack = []
        result = 0
        sign = 1
        i = 0

        while i<len(s):
            if s[i].isdigit():
                num = 0

                while i<len(s) and s[i].isdigit():
                    num*=10
                    num+=int(s[i])
                    i+=1

                i-=1
                result+=sign*num

            elif s[i] == '+':
                sign = 1

            elif s[i] == '-':
                sign = -1

            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif s[i] == ')':
                result*=stack.pop()
                result+=stack.pop()
                
            i+=1
        
        return result

sol = Solution()
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))