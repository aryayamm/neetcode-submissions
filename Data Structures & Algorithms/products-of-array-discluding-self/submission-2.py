class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        lefty = nums[0]
        for i in range(1, len(nums)-1):
            lefty *= nums[i]
            left.append(lefty)
        right = [nums[-1]]
        righty = nums[-1]
        for i in range(len(nums)-2,0,-1 ):
            righty *= nums[i]
            right.append(righty)
        
        ans = []
        right = right[::-1]
        
        for i in range(len(nums)):
            if i == 0:
                ans.append(right[0])
                continue
            if i == len(nums)-1:
                ans.append(left[-1])
                continue
            ans.append(left[i-1]*right[i])
        return ans