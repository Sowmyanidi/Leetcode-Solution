class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        indices = []
        count = [0]*len(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
                indices.append(i)
            elif s[i]==')' and len(stack)!=0:
                stack.pop()
                ind = indices.pop()
                count[ind]+=1
                count[i]+=1
        
        max_length = 0
        total = 0
        for i in range(len(count)):
            if count[i]==0:
                max_length = max(max_length, total)
                total = 0
            elif count[i]==1:
                total+=1
        
        return max(max_length, total)

sol = Solution()
print(sol.longestValidParentheses(")()())"))