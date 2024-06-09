'''
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''

#comment lines shortcut: CTRL+/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            if len(nums) == 1:
                return 0
            else:
                return nums.index(max(nums))

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print("Peak Element Index:",sol.findPeakElement([1,2,3]))


# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             if len(nums) == 1:
#                 return 0
#             else:
#                 return nums.index(max(nums[0], nums[1]))

#         mid = len(nums)//2
#         if (nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]):
#             return mid
#         elif nums[mid-1]>nums[mid]:
#             return self.findPeakElement(nums[:mid])
#         elif nums[mid+1]>nums[mid]:
#             return self.findPeakElement(nums[mid+1:])