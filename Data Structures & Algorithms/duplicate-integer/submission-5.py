class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = {}
        i = 0
        while i < len(nums):
            curr_number = nums[i]
            if seen_numbers.get(curr_number)== None:
                seen_numbers[curr_number] = True
            else:
                return True
            i += 1
        return False