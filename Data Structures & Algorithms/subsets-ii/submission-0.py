class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(arr, i):
            if i == len(nums):
                if arr not in ans:
                    ans.append(arr)
                return
            solve(arr + [nums[i]], i+1)
            solve(arr, i+1)

        nums.sort()
        solve([],0)

        return ans