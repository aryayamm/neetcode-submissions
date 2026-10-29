class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        best = 0
        for i in nums:
            if i-1 not in num:
                n = 1
                while i + n in num:
                    n+= 1
                best = max(best,n)
        return best