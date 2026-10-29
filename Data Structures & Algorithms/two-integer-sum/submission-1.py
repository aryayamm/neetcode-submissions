class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):

            if (target-nums[i]) not in table:
                table[nums[i]] = i
            else:
                return [table[target-nums[i]], i ]
        