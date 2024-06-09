'''
class Solution:
    def compress(self, chars: list[str]) -> int:
        length = len(chars)
        count = 0
        for i in range(length):
            if i<length-1 and chars[i]==chars[i+1]:
                count+=1
            else:
                count+=1
                chars.append(chars[i])
                if count>1:
                    for j in str(count):
                        chars.append(j)
                count=0
        
        del chars[0:length]
        return len(chars)
'''

class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i<len(chars):
            grouplength = 0
            char = chars[i]

            while i<len(chars) and chars[i]==char:
                grouplength += 1
                i+=1
            chars[res]=char
            res+=1

            if grouplength>1:
                for digit in str(grouplength):
                    chars[res]=digit
                    res+=1
        return res
    
sol = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
res = sol.compress(chars)
print(chars)