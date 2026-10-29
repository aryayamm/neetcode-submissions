class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(arr, total, i):
            if total == target:
                ans.append(arr)
                return
            if total > target or i == len(nums):
                return

            solve(arr+[nums[i]], total + nums[i], i)
            solve(arr, total, i+1)


        solve([],0,0)
        return ans
        