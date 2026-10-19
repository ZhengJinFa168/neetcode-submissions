class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        l = 0
        n_max = 0
        res = 0
        
        for r in range(len(nums)):
            if nums[r] == max_num:
                n_max += 1
            while n_max == k:
                if nums[l] == max_num:
                    n_max -= 1
                l += 1
            res += l
            
        return res