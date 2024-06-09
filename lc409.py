class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for i in s:
            if i not in hashmap.keys():
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        odd = 0
        length = 0
        for i in hashmap.keys():
            if hashmap[i]%2!=0:
                odd = 1
                length += hashmap[i]-1
            else:
                length += hashmap[i]
        
        if odd==1:
            return length+1
        return length

sol = Solution()
print(sol.longestPalindrome("abccccdd"))