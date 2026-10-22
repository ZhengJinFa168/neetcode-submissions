class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix.append(product)
            product *= nums[i]
        product = 1
        res = []
        for i in range(len(nums)):
            res.append(suffix[len(nums)-1-i]*product)
            product *= nums[i]
        
        return res