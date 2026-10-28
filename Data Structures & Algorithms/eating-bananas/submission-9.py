class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        res = r
        while l <= r:
            mid = (l+r)//2
            h_taken = 0
            for n in piles:
                h_taken += math.ceil(n/mid)
            if h_taken <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res