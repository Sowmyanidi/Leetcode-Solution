class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ind_t = 0
        ind_s = 0
        while ind_s<len(s) and ind_t<len(t):
            if s[ind_s]==t[ind_t]:
                ind_t+=1
            ind_s+=1
        return len(t)-ind_t

sol = Solution()
print(sol.appendCharacters("ajkhe", "juh"))