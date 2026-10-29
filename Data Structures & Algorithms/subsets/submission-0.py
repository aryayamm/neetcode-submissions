class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(arr, n):
            if n == len(nums):
                ans.append(arr)
                return
            solve(arr + [nums[n]], n+1)
            solve(arr, n+1)

        solve([],0)
        return ans
