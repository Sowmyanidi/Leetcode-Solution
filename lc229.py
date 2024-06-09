class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap.keys():
                hashmap[i]=1
            else:
                hashmap[i]+=1
        res = []
        n = len(nums)//3
        for i in hashmap.keys():
            if hashmap[i]>n:
                res.append(i)
        return res

sol = Solution()
print(sol.majorityElement([3,2,3]))