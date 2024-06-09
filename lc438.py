class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_len = len(p)
        
        if p_len>len(s):
            return []

        indices = []
        freq = {}

        for i in p:
            if i not in freq.keys():
                freq[i]=1
            else:
                freq[i]+=1
        
        sub = {}
        for i in range(p_len):
            if s[i] not in sub.keys():
                sub[s[i]]=1
            else:
                sub[s[i]]+=1

        if sub == freq:
            indices.append(0)

        for i in range(p_len, len(s)):
            j = i-p_len
            sub[s[j]]-=1

            if sub[s[j]]==0:
                sub.pop(s[j])

            if s[i] not in sub:
                sub[s[i]]=1
            else:
                sub[s[i]]+=1

            if sub==freq:
                indices.append(j+1)
        return indices

sol = Solution()
print(sol.findAnagrams("aaaaaaaaaa", "aaa"))