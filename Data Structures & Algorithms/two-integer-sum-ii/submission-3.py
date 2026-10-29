class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        count = 0
        while left < right:
            a = numbers[left] + numbers[right]
            if a > target:
                right -= 1
            elif a < target:
                left += 1
            elif a == target:
                print(left+1,right+1)
                return [left+1,right+1]