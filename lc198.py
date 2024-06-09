class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==2:
            return max(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0

        back_dp = [0]*len(nums)
        back_dp[0] += nums[0]
        back_dp[1] += max(nums[0], nums[1])

        for i in range(2, len(nums)):
            back_dp[i] += max(back_dp[i-1], back_dp[i-2]+nums[i])
        return back_dp[-1]

sol = Solution()
print(sol.rob([2,1,1,2]))