class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        temp = sorted(nums)
        l,r = 0,len(temp) - 1
        i = 0
        while l < r:
            nums[i] = temp[l]
            i += 1
            l += 1
            nums[i] = temp[r]
            r -= 1
            i += 1
        return
        