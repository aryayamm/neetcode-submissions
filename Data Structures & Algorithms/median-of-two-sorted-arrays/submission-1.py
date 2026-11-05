class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            x = (lo + hi) // 2
            y = half - x

            Aleft  = A[x - 1] if x > 0 else float("-inf")
            Aright = A[x]     if x < m else float("inf")
            Bleft  = B[y - 1] if y > 0 else float("-inf")
            Bright = B[y]     if y < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                hi = x - 1
            else:
                lo = x + 1