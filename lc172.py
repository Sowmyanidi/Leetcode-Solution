class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        zeros = 0
        while n>0:
            zeros +=n//5
            n//=5
        return zeros

sol = Solution()
print(sol.trailingZeroes(64))