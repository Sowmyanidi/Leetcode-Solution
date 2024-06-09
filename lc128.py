'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        counts = []
        for i in nums:
            count = 0
            if i-1 not in s:
                while i in s:
                    count+=1
                    i+=1
            counts.append(count)
        return max(counts)
    
sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))