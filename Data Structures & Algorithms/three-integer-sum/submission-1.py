class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = {}
        output = []
        i=0
        lenght = len(nums)
        while i < lenght - 2:
            left_pointer = i + 1
            right_pointer = lenght - 1
            while left_pointer < right_pointer:
                first_num = nums[i]
                second_num = nums[left_pointer]
                third_num = nums[right_pointer]
                sum_of_nums = first_num + second_num + third_num
                if sum_of_nums == 0:
                    t = (first_num,second_num,third_num)
                    hashmap[t] = 1
                    left_pointer += 1
                elif sum_of_nums > 0:
                    right_pointer -= 1
                else:
                    left_pointer += 1
            i += 1

        for key,value in hashmap.items():
            output.append(list(key))
        
        return output

        