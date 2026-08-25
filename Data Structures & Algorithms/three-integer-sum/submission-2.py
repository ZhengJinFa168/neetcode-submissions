class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i=0
        lenght = len(nums)
        print(nums)
        while i < lenght - 2:
            prev_i = i
            if nums[i] > 0:
                break
            right_pointer = lenght - 1
            left_pointer = i + 1

            while left_pointer < right_pointer:
                first_num = nums[i]
                second_num = nums[left_pointer]
                third_num = nums[right_pointer]
                sum_of_nums = first_num + second_num + third_num
                if sum_of_nums == 0:
                    t = [first_num,second_num,third_num]
                    output.append(t)
                    prev_left_pointer = left_pointer
                    left_pointer += 1
                    right_pointer -= 1
                    while nums[left_pointer] == nums[prev_left_pointer] and left_pointer < right_pointer:
                        left_pointer += 1
                elif sum_of_nums > 0:
                    right_pointer -= 1
                else:
                    prev_left_pointer = left_pointer
                    left_pointer += 1
                    while nums[left_pointer] == nums[prev_left_pointer] and left_pointer < right_pointer:
                        left_pointer += 1
            i += 1
            while nums[prev_i] == nums[i] and i< lenght - 2:
                i += 1

        return output

        