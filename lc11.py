class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        capacity = 0
        while (left<right):
            capacity = max(capacity, min(height[left], height[right])*(right-left))
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        
        return capacity

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))


'''
Hint 1
If you simulate the problem, it will be O(n^2) which is not efficient.

Hint 2
Try to use two-pointers. 
Set one pointer to the left and one to the right of the array. 
Always move the pointer that points to the lower line.

Hint 3
How can you calculate the amount of water at each step?
'''