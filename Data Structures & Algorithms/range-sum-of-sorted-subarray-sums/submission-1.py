class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            res.append(cur)
            for j in range(i+1,len(nums)):
                cur += nums[j]
                res.append(cur)
        res.sort()
        return sum(res[left-1:right])%1000000007