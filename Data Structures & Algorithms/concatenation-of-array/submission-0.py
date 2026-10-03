class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        j = 0
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i]) 

        return ans

        