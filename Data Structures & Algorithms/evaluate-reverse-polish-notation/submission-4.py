class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+","-","/","*"}
        res = None
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in operands:
                second_val = stack.pop()
                first_val = stack.pop()
                if i == "+":
                    res = int(first_val) + int(second_val)
                elif i == "-":
                    res = int(first_val) - int(second_val)
                elif i == "*":
                    res = int(first_val) * int(second_val)
                else:
                    res = int(int(first_val) / int(second_val))
                stack.append(res)
            else:
                stack.append(i)
        return res
        
