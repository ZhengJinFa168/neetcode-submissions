class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            if hashtable.get(i,0):
                return i
            else:
                hashtable[i] = 1
            
        return 0