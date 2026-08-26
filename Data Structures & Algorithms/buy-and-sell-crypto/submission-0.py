class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        left_pointer = 0
        right_pointer = 1
        possible_left_pointer = 0
        while left_pointer < len (prices)-1:
            right_pointer = left_pointer + 1
            today = prices[left_pointer]
            future = prices[right_pointer]
            diff = future - today
            if(diff <= 0):
                left_pointer += 1
                right_pointer += 1
            else:
                while right_pointer < len (prices):
                    future = prices[right_pointer]
                    diff = future - today
                    if (diff > output):
                        output = diff
                    if(future < today):
                        possible_left_pointer = right_pointer
                    else:
                        possible_left_pointer = left_pointer + 1
                    right_pointer += 1
                left_pointer = possible_left_pointer
        return output
                

        