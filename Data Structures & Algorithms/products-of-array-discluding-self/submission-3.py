class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 0
        flag = False
        two_zero = False
        for num in nums:
            if prod == 0 and num != 0:
                prod += num 
            else:
                if num == 0:
                    if flag:
                        two_zero = True
                    flag = True
                    continue
                prod *= num
        for num in nums:
            if two_zero:
                output.append(0)
            elif num == 0:
                output.append(prod)
            else:
                if flag == True:
                    output.append(0)
                else:
                    output.append(int(prod/num))
        return output
