class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(arr):
            if len(arr) == len(nums):
                ans.append(arr)
                return
            for i in nums:
                if i not in arr:
                    solve(arr + [i])
        solve([])
        return ans