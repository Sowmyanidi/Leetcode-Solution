class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)==1:
            return [strs]
        else:
            hashmap = {}
            for i in strs:
                key = ''.join(sorted(i))                            #Categorize by sorting (method 1)
                if key not in hashmap.keys():                       #Time complexity: O(n*mlog(m))  --> n = length of strs
                    hashmap[key]=[]                                 #                               --> m = average length of string in strs
                    hashmap[key].append(i)
                else:
                    hashmap[key].append(i)
            return hashmap.values()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))