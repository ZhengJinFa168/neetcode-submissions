class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        l = 0
        r = 1
        while r < len(prices):
            today = prices[l]
            future = prices[r]
            if(future < today):
                l = r
            else:
                diff = future - today
                output = max(output,diff) 
            r += 1
        
        return output