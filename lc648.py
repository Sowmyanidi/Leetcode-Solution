class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        
        li = sentence.split()

        for i in range(len(li)):
            for word in dictionary:
                if li[i].startswith(word):
                    li[i] = min(li[i], word)
        
        return ' '.join(li)

sol = Solution()
print(sol.replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery"))