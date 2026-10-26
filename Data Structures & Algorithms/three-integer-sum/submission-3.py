class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        lung = len(nums)
        for i in range(lung-2):
            l, r = i+1,lung-1
            while l < r:
                tot = nums[i]+nums[l]+nums[r]
                if tot == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1
        final = []
        for el in res:
            final.append(list(el))
        return final