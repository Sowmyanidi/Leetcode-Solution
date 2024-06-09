class Solution:
    def clumsy(self, n: int) -> int:
        stack = ['-','+','/','*']
        fact = n
        n-=1
        res = 0
        count = 0
        while n>0:
            op = stack.pop()
            if op=='*':
                fact*=n
            elif op=='/':
                fact//=n
            elif op=='+':
                fact+=n
            elif op=='-':
                count+=1
                if count==1:
                    res = fact
                    fact = n
                else:
                    res-=fact
                    fact = n
            if len(stack)==0:
                stack.append('-')
                stack.append('+')
                stack.append('/')
                stack.append('*')
            n-=1
        return res-fact
sol = Solution()
print(sol.clumsy(10))