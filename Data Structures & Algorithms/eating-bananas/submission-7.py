class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hour = 0
            for i in piles:
                hour += (i + k-1) // k
            return hour 

        l = 1
        r = max(piles)
        ans = r

        while l <= r :
            mid = (l+r)//2
            c = check(mid)
            if c <= h:
                r = mid - 1 
                ans = mid
            elif c > h:
                l = mid + 1
        return ans
