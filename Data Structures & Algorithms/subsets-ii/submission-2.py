class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def solve(arr, i):
            if i == len(nums):
                if arr not in ans:
                    ans.append(arr)
                return
            solve(arr + [nums[i]], i+1)
            solve(arr, i+1)
        solve([],0)

        return ans