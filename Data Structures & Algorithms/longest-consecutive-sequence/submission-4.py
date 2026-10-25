class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        res = 1
        maxNum = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] + 1:
                res += 1
                maxNum = max(maxNum,res)
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = 1
        
        return maxNum