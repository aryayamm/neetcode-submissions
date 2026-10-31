class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l = 0
        r = n - 1
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if mid+1 == n:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]

            if mid-1 < 0:
                if nums[mid] < nums[mid+1]:
                    return nums[mid]

            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[r]:
                r = mid-1
            else:
                l = mid+1