class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+","-","*","/"}
        for el in tokens:
            if not el in operands:
                stack.append(int(el))
            else:
                second = stack.pop()
                first = stack.pop()
                if el == "+":
                    stack.append(first + second)
                elif el == "-":
                    stack.append(first - second)
                elif el == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
        
        return stack.pop()