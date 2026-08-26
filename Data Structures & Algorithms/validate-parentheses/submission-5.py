class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        for par in s:
            if (par == ")" or par == "]" or par == "}") and len(stack) == 0:
                    return False
            if (par == "(" or par == "[" or par == "{" ):
                stack.append(par)
            else:
                last_el = stack.pop()
                if par == ")" and last_el != "(":
                    return False
                elif par == "]" and last_el != "[":
                    return False
                elif par == "}" and last_el != "{":
                    return False
        if len(stack) > 0:
            return False
        return True