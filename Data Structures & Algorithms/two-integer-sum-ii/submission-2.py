class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(n):
            low = 0
            high = len(numbers) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] == n:
                    return mid
                elif numbers[mid] < n:
                    low = mid + 1
                else:
                    high = mid - 1

        for i in range(len(numbers)):
            j = search(target-numbers[i])
            if j is not None and i != j:
                if i < j:
                    return[i+1,j+1]
                else:
                    return[j+1,i+1]             