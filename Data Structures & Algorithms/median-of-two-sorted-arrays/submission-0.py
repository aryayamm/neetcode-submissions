class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = (len(nums1) + len(nums2))//2 
        arr = []
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] < nums2[0]:
                arr.append(nums1[0])
                nums1.pop(0)
            else:
                arr.append(nums2[0])
                nums2.pop(0)
        if len(nums1) != 0:
            for i in nums1:
                arr.append(i)
        else:
            for i in nums2:
                arr.append(i)
        if len(arr) % 2 == 1:
            return arr[m]
        else:
            return (arr[m - 1] + arr[m])/2
