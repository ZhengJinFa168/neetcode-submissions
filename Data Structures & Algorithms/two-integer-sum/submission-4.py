class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                temp = j + i + 1
                sum_of_nums = nums[i] + nums[temp]
                if sum_of_nums == target:
                    return [i,temp]

        return [0,0]
                
        