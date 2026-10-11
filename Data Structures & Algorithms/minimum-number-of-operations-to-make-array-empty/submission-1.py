class Solution:
    def minOperations(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            table[n] = table.get(n,0) + 1

        res = 0
        for val in table.values():
            if val == 1:
                return -1
            diff = val % 3
            n = val // 3
            if diff == 0:
                res += n
            elif diff == 1:
                res += n - 1 + 2
            else:
                res += n + 1 
            
        return res
