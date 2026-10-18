class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minPenalty = 0
        for cust in customers:
            if cust == "N":
                minPenalty += 1
        j = len(customers)
        penalty = minPenalty
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == "Y":
                penalty += 1
            else:
                penalty -= 1
            if penalty <= minPenalty:
                minPenalty = penalty
                j = i
        
        return j
                
