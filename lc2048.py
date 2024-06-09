class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n>=666666:
            return 1224444
        for i in range(n+1, 666666+1):
            sub = str(i)
            flag = False
            for digit in sub:
                if sub.count(digit)!=int(digit):
                    flag = False
                    break
                else:
                    flag = True
            if flag == True:
                return i

sol = Solution()
print(sol.nextBeautifulNumber(555555))