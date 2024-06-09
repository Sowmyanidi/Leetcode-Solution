class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words)==0:
            return []
        elif len(words)==1:
            return words[0].split()
            
        hashmap = {}
        for i in words[0]:
            if all(i in word for word in words):
                if i not in hashmap.keys():
                    hashmap[i] = float("inf")

        for i in hashmap.keys():
            for word in words:
                if word.count(i) < hashmap[i]:
                    hashmap[i] = word.count(i)

        res = []
        for i in hashmap.keys():
            while hashmap[i] > 0:
                res.append(i)
                hashmap[i] -= 1
        
        return res

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))