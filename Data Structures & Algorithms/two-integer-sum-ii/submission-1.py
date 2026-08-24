class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        max_lenght = len(numbers) - 1

        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            sum_num = numbers[left_pointer] + numbers[right_pointer]
            
            if sum_num == target:
                return [left_pointer+1,right_pointer+1]
            elif sum_num > target:
                right_pointer -= 1
            else:
                left_pointer += 1
        return [right_pointer]
        