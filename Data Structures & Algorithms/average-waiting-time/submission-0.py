class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        sum_times = 0
        for cust in customers:
            curr_time = max(curr_time,cust[0])
            finished_time = curr_time + cust[1]
            diff = finished_time - cust[0]
            sum_times += diff
            curr_time = finished_time
        
        return sum_times / len(customers)
        
        