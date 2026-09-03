class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_array = sorted(nums)
        print(sorted_array)
        i = 1
        maximum = 0
        prev = sorted_array[0]
        temp = 1
        while i < len(sorted_array):
            if(sorted_array[i] == prev):
                i += 1
            elif (sorted_array[i] == prev + 1 ):
                prev = sorted_array[i]
                i += 1
                temp += 1
            elif (temp == 1):
                prev = sorted_array[i]
                i += 1
            else:
                if temp > maximum:
                    maximum = temp
                temp = 1
                prev = sorted_array[i]
                i += 1
        if temp > maximum:
            maximum = temp

        return maximum