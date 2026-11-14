class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1,max(piles)
        res = r
        while l < r:
            mid = (r + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                res = min(res,mid)
                r = mid
            else:
                l = mid + 1
        
        return res
