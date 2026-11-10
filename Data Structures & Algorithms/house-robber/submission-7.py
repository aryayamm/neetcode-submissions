class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        tot = 0
        p = [-1]*len(nums)
        def rob(n, cur, dp):
            nonlocal tot, nums
            cur += nums[n]
            if cur <= dp[n]:
                return tot
            dp[n] = cur
            tot = max(tot, cur)
            if n + 2 < len(nums):
                rob(n+2, cur, dp)
            if n + 3 < len(nums):
                rob(n+3, cur, dp)
            return tot
        rob(0,0, p)
        rob(1,0, p)
        return tot