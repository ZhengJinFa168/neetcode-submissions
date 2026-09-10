class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max (piles)
        l = 1
        res = r

        while l <= r:
            k = (r + l)//2
            h_taken = 0
            for pile in piles:
                h_taken += math.ceil(pile/k)
            if h_taken <= h:
                res = k
                r = k - 1
            else:
                l = k + 1 
        return res
            
            
            
            

        

